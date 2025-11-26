from abc import ABC, abstractmethod
from redis.asyncio import Redis

class AbcRefreshToken(ABC):
    
    def __init__(self, redis: Redis):
        self.redis = redis
    
    def _key(self, sid: str):
        return f"refresh:{sid}"
    
    @abstractmethod
    async def save(self, sid: str, user_id: int, ttl_second: int):
        raise NotImplementedError()
        
    @abstractmethod
    async def get(self, sid: str):
        raise NotImplementedError()
        
    @abstractmethod
    async def delete(self, sid: str):
        raise NotImplementedError()