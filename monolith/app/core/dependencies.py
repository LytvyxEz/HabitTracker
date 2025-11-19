from fastapi import HTTPException, Cookie, status
from typing import Optional
from monolith.app.api.auth.schemas import UserResponse
from monolith.app.core.jwt import JWT 


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