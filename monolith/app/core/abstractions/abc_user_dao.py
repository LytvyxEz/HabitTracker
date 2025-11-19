from abc import ABC, abstractmethod


class AbcUserDAO(ABC):
    @abstractmethod    
    async def get_by_email():
        raise NotImplementedError()
        
    @abstractmethod
    async def create_user():
        raise NotImplementedError()
        
    @abstractmethod
    async def save_refresh_token():
        raise NotImplementedError()
        
    @abstractmethod
    async def delete_refresh_token():
        raise NotImplementedError()
        
    @abstractmethod
    async def get_refresh_token():
        raise NotImplementedError()
        