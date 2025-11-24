from redis.asyncio import Redis
from .config import settings

r = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    decode_responses=True
)