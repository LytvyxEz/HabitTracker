from abc import ABC, abstractmethod


from ...api.auth.schemas import UserResponse
from ...repository.refresh_token import RefreshTokenDAO
from ...repository.user import UserDAO
from ...core.dependencies import JWT, HashManager

class AbcAuthService(ABC):
    
    def __init__(self, user_dao: UserDAO, refresh_dao: RefreshTokenDAO, jwt_manager: JWT, hash_manager: HashManager):
        self.user_dao = user_dao 
        self.refresh_repo = refresh_dao
        self.jwt_manager = jwt_manager
        self.hash_manager = hash_manager
    
    @abstractmethod
    async def create_tokens(self, user: UserResponse):
        raise NotImplementedError()
    
    
    @abstractmethod
    async def refresh_token_check(self, refresh_token: str):
        raise NotImplementedError()
    
    
    @abstractmethod
    async def create_user(self, user_data):
        raise NotImplementedError()
    
    @abstractmethod
    async def login_user(self):
        raise NotImplementedError()
        
    
    @abstractmethod
    async def logout_user(self, user):
        raise NotImplementedError()