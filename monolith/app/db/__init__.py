from fastapi import FastAPI
from contextlib import asynccontextmanager
from .session import database

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()