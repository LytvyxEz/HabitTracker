from fastapi import APIRouter, Depends

from ...schemas import UserResponse
from ...core.dependencies import get_current_user


router = APIRouter(prefix='/user')


@router.get('/me')
async def get_me(user: UserResponse = Depends(get_current_user)):
    return user

