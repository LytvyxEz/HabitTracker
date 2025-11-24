from bcrypt import hashpw, checkpw, gensalt
from asyncio import to_thread

from app.core.abstractions import AbstractHashManager

class HashManager(AbstractHashManager):
    @staticmethod
    async def check_password(password: str, hashed_password: bytes) -> bool:
        return await to_thread(checkpw, password.encode('utf-8'), hashed_password)

    @staticmethod        
    async def hash_password(password: str | bytes) -> bytes:
        if isinstance(password, str):
            password = password.encode('utf-8')
        return await to_thread(hashpw, password, gensalt())




