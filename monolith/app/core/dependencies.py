from fastapi import HTTPException, Cookie, status, Depends

from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from monolith.app.core.jwt import JWT 
from monolith.app.api.auth.schemas import UserResponse
from monolith.app.db.session import get_db
from monolith.app.repository.user import UserDAO
from monolith.app.api.auth.service import AuthService
from monolith.app.core.hashing import HashManager

def get_current_user(access_token: Optional[str] = Cookie(None)) -> UserResponse:
    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing access token cookie",
            headers={"WWW-Authenticate": "Bearer"},
        )
    try:
        payload = JWT.decode_jwt(access_token)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid or expired token: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return UserResponse(
        id=int(payload["sub"]),      
        email=payload["email"],       
        username=payload["username"]  
    )
    

async def get_user_dao(db: AsyncSession = Depends(get_db)) -> UserDAO:
    return UserDAO(db)


async def get_auth_service(db: AsyncSession = Depends(get_db)) -> AuthService:
    user_dao = UserDAO(db)
    return AuthService(user_dao=user_dao)


async def get_hash_manager() -> HashManager:
    return HashManager()

async def get_jwt_manager() -> JWT:
    return JWT()