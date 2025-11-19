from abc import ABC, abstractmethod

from redis.asyncio import Redis

from ..redis import r

class AbcRefreshToken(ABC):
    
    def __init__(self, redis: Redis = r):
        self.redis = redis
    
    def _key(self, jti: str):
        raise f"refresh:{jti}"
    
    @abstractmethod
    async def save(self, jti: str, user_id: int, ttl_second: int):
        raise NotImplementedError()
        
    @abstractmethod
    async def exists(self, jti: str):
        raise NotImplementedError()
        
    @abstractmethod
    async def delete(self, jti: str):
        raise NotImplementedError()