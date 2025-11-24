from fastapi import APIRouter, Request, Depends, Response, HTTPException

from .schemas import UserResponse, LoginSchema, RegisterSchema
from .service import AuthService
from ...core.abstractions import UserNotFoundError, UserAlreadyExistsError, InvalidCredentials, UserDoesNotExistsError
from ...core.dependencies import get_current_user, get_auth_service, prevent_authenticated_access, get_sid


router = APIRouter(prefix='/auth')


@router.post('/register')
async def register(
    request: Request,
    user_data: RegisterSchema,
    auth_service: AuthService = Depends(get_auth_service),
    _: None = Depends(prevent_authenticated_access)
):
    try:
        user = await auth_service.create_user(user_data)
        return {'message': 'Succesfully created account'}
    except (UserAlreadyExistsError, UserNotFoundError) as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post('/login')
async def login(
    response: Response,
    user_data: LoginSchema,
    auth_service: AuthService = Depends(get_auth_service),
    _: None = Depends(prevent_authenticated_access)
):
    try:
        user, access_token = await auth_service.login_user(user_data)
    
        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            secure=True,  
            samesite="lax",
            max_age=15 * 60, 
        )

        return {'message': 'Succesfully logged in'}
    except (UserAlreadyExistsError, UserNotFoundError, InvalidCredentials, UserDoesNotExistsError) as e:
        raise HTTPException(status_code=400, detail=str(e))



@router.post("/refresh")
async def refresh(
    response: Response,
    auth_service: AuthService = Depends(get_auth_service)
):
    ... #TODO
    
    
@router.post('/logout')
async def logout(
    response: Response,
    sid: str=Depends(get_sid),
    user: UserResponse = Depends(get_current_user),
    auth_service: AuthService = Depends(get_auth_service)
                 ):
    try:
        await auth_service.logout_user(user, sid)
        
        response.delete_cookie(
            'access_token',
            path="/",
            domain=None,
            secure=True,
            httponly=True,
            samesite="lax"
            )
        
        return {'message': 'Succesfully logged out'}
    except (UserAlreadyExistsError, UserNotFoundError) as e:
        raise HTTPException(status_code=400, detail=str(e))