from abc import ABC, abstractmethod


from ...api.auth.schemas import UserResponse
from ...repository.refresh_token import refresh_token_manager
from ...repository.user import user_dao_manager


class AbcAuthService(ABC):
    
    def __init__(self):
        self.refresh_repo = refresh_token_manager
        self.user_repo = user_dao_manager
    
    
    @abstractmethod
    async def create_tokens(user: UserResponse):
        raise NotImplementedError()
    
    
    @abstractmethod
    async def refresh_token_check(refresh_token: str):
        raise NotImplementedError()