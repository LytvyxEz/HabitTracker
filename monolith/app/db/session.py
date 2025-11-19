from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from contextlib import asynccontextmanager

from ..core.config import settings

class Database:
    def __init__(self):
        self.engine = create_async_engine(settings.DATABASE_URL, echo=True)
        self.SessionLocal = async_sessionmaker(bind=self.engine, autoflush=False, autocommit=False)
    
    
    @asynccontextmanager
    async def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            await db.close()


database = Database()

async def get_db():
    async with database.get_db() as session:
        yield session