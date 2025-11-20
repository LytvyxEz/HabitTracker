
from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from ...api.auth.schemas import RegisterSchema

class AbcUserDAO(ABC):
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    @abstractmethod    
    async def get_by_email(self, email: str):
        raise NotImplementedError()
        
    @abstractmethod
    async def create_user(self, user: RegisterSchema):
        raise NotImplementedError()
    
    
    @abstractmethod
    async def get_by_id(self, user_id: int):
        raise NotImplementedError()