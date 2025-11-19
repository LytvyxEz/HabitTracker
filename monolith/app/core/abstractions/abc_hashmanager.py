from abc import ABC, abstractmethod

class AbstractHashManager(ABC):
    
    @abstractmethod
    async def check_password(password: str, hashed_password: bytes) -> bool:
        raise NotImplementedError()
    
    @abstractmethod
    async def hash_password(password: str | bytes) -> str | bytes:
        raise NotImplementedError()
    