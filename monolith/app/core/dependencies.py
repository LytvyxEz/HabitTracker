from fastapi import HTTPException, Cookie, status, Depends
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from ..api.auth.schemas import UserResponse
from ..db.session import get_db

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

def get_sid(access_token: Optional[str] = Cookie(None)) -> str:
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
    
    if not payload['sid']:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid or expired token: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"},
        )  
    
    return payload['sid']
    
    
def prevent_authenticated_access(access_token: Optional[str] = Cookie(None)) -> None:
    if access_token:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='You are already logged in'
        )
   

from .hashing import HashManager
def get_hash_manager() -> HashManager: 
    return HashManager()

from .jwt import JWT 
def get_jwt_manager() -> JWT: 
    return JWT()

from ..repository.user import UserDAO
def get_user_dao(db: AsyncSession = Depends(get_db)) -> UserDAO: 
    return UserDAO(db)

from ..repository.refresh_token import RefreshTokenDAO
def get_refresh_dao() -> RefreshTokenDAO:
    return RefreshTokenDAO() 

def get_auth_service(
            user_dao: UserDAO = Depends(get_user_dao),
            refresh_dao: RefreshTokenDAO = Depends(get_refresh_dao),
            jwt_manager: JWT = Depends(get_jwt_manager),
            hash_manager: HashManager = Depends(get_hash_manager)
            ) -> "AuthService": # pyright: ignore[reportUndefinedVariable]
    
    from ..api.auth.service import AuthService
    
    return AuthService(user_dao=user_dao, refresh_dao=refresh_dao, jwt_manager=jwt_manager, hash_manager=hash_manager)
