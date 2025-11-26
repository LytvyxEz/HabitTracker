from ..core.abstractions import AbcRefreshToken
from ..core.redis import r


class RefreshTokenDAO(AbcRefreshToken):
    def __init__(self, redis=r):
        super().__init__(redis)
    
    async def save(self, sid: str, user_id: int, ttl_second: int = 14 * 24 * 60 * 60) -> None: 
        await self.redis.set(self._key(sid), user_id, ex=ttl_second)
        
        
    async def get(self, sid: str) -> str:
        value = await self.redis.get(self._key(sid))
        
        return value if value else None
        
    async def delete(self, sid: str) -> None:
        await self.redis.delete(self._key(sid))
        