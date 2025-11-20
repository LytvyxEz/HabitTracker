from abc import ABC, abstractmethod


from ...api.auth.schemas import UserResponse
from ...repository.refresh_token import RefreshTokenDAO
from ...repository.user import UserDAO
from ...core.dependencies import JWT


class AbcAuthService(ABC):
    
    def __init__(self, user_dao: UserDAO, refresh_dao: RefreshTokenDAO, jwt_manager: JWT):
        self.user_dao = user_dao 
        self.refresh_repo = refresh_dao
        self.jwt_manager = jwt_manager
    
    @abstractmethod
    async def create_tokens(user: UserResponse):
        raise NotImplementedError()
    
    
    @abstractmethod
    async def refresh_token_check(refresh_token: str):
        raise NotImplementedError()
    
    
    @abstractmethod
    async def create_user():
        raise NotImplementedError()
    
    @abstractmethod
    async def login_user():
        raise NotImplementedError()
        
    
    @abstractmethod
    async def logout_user():
        raise NotImplementedError()