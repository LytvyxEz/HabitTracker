from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine
from contextlib import asynccontextmanager
from typing import Optional
from ..core.config import settings

class Database:
    def __init__(self):
        self.engine: Optional[AsyncEngine] = None
        self.SessionLocal = None
    
    async def connect(self):
        self.engine = create_async_engine(
            settings.DATABASE_URL, 
            echo=True,
            pool_pre_ping=True,
            pool_size=5,
            max_overflow=10
        )
        self.SessionLocal = async_sessionmaker(
            bind=self.engine, 
            autoflush=False, 
            autocommit=False,
            expire_on_commit=False
        )
    
    async def disconnect(self):
        if self.engine:
            await self.engine.dispose()
            self.engine = None
            self.SessionLocal = None
    
    @asynccontextmanager
    async def get_db(self):
        if not self.SessionLocal:
            raise RuntimeError("Database not connected. Call connect() first.")
        
        db = self.SessionLocal()
        try:
            yield db
        finally:
            await db.close()

database = Database()

async def get_db():
    async with database.get_db() as session:
        yield session