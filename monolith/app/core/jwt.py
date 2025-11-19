from jwt import encode, decode
from datetime import datetime, timezone, timedelta
import uuid

from app.core.config import settings
from app.core.abstractions import AbcJWT
from app.api.auth.schemas import UserResponse


class JWT(AbcJWT):
    @staticmethod
    def encode_jwt(user: UserResponse, token_type: str, expire_minutes: int):
        now = datetime.now(timezone.utc)

        payload = {
            "sub": str(user.id),
            "email": user.email,   
            "username": user.username, 
            "jti": uuid.uuid4().hex,
            "iat": int(now.timestamp()),
            "exp": int((now + timedelta(minutes=expire_minutes)).timestamp()),
            "typ": token_type,
            "iss": "auth_service",
            "aud": "users"
        }

        return encode(payload, settings.SECRET_KEY, algorithm=settings.TOKEN_ALG)

    @staticmethod
    def decode_jwt(token: str):
        if token.startswith("Bearer "):
            token = token.split(" ", 1)[1]

        return decode(
            token,
            key=settings.SECRET_KEY,
            algorithms=[settings.TOKEN_ALG],
            audience="users",
            issuer="auth_service"
        )

    @classmethod
    def create_tokens(cls, user: UserResponse):
        access_token = cls.encode_jwt(user, "access", expire_minutes=15)
        refresh_token = cls.encode_jwt(user, "refresh", expire_minutes=60 * 24 * 7)
        return access_token, refresh_token


jwt_manager = JWT()