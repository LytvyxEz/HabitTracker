from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, computed_field
from typing import Literal


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )
    
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_DATABASE: str
    
    TOKEN_ALG: str
    SECRET_KEY: str
    
    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_DATABASE}"
        )



settings = Settings()