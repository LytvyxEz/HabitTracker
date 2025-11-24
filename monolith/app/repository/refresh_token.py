from ..core.abstractions import AbcRefreshToken
from ..core.redis import r


class RefreshTokenDAO(AbcRefreshToken):
    def __init__(self, redis=r):
        super().__init__(redis)
    
    async def save(self, sid: str, user_id: int, ttl_second: int = 14 * 24 * 60 * 60): 
        await self.redis.set(self._key(sid), user_id, ex=ttl_second)
        
    async def exists(self, sid: str):
        value = await self.redis.get(self._key(sid))
        return value.decode('utf-8') if value else None
        
    async def delete(self, sid: str):
        await self.redis.delete(self._key(sid))