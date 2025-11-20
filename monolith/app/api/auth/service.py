from fastapi import HTTPException

from ...core.abstractions import AbcAuthService
from ..auth.schemas import UserResponse

class AuthService(AbcAuthService):    
    
    async def create_tokens(self, user: UserResponse):
        access, refresh = self.jwt_manager.create_tokens(user)

        refresh_payload = self.jwt_manager.decode_jwt(refresh)
        
        jti = refresh_payload["jti"]

        ttl = refresh_payload["exp"] - refresh_payload["iat"]

        await self.refresh_repo.save(jti, user.id, ttl_seconds=ttl)

        return access, refresh
    
    
    async def refresh_token_check(self, refresh_token: str):
        payload = self.jwt_manager.decode_jwt(refresh_token)

        if payload["typ"] != "refresh":
            raise HTTPException(401, "Wrong token type")

        jti = payload["jti"]

        user_id = await self.refresh_repo.exists(jti)
        if not user_id:
            raise HTTPException(401, "Refresh token expired or revoked")

        await self.refresh_repo.delete(jti)

        user = await self.user_dao.get_by_id(int(payload["sub"]))

        access, refresh = await self.create_tokens(user)

        return {
            "access": access,
            "refresh": refresh
        }
        