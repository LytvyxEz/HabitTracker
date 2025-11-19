from ..core.abstractions import AbcRefreshToken


class RefreshToken(AbcRefreshToken):
    def __init__(self):
        super().__init__()
        
    
    async def save(self, jti: str, user_id: int, ttl_second: int = 14 * 60* 60):
        await self.redis.set(self._key(jti), user_id, ex=ttl_second)
        
    async def exists(self, jti: str):
        return await self.redis.get(self._key(jti))
        
    async def delete(self, jti: str):
        await self.redis.delete(self._key(jti))
        
        
refresh_token_manager = RefreshToken()