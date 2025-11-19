from abc import ABC, abstractmethod
from pydantic import EmailStr
from typing import Any

class AbcJWT(ABC):
    @abstractmethod
    @staticmethod
    def encode_jwt(email: EmailStr) -> str:
        raise NotImplementedError()
    
    @abstractmethod
    @staticmethod
    def decode_jwt(token: str) -> Any:
        raise NotImplementedError()
        
    
    @classmethod
    def create_tokens(cls, email: EmailStr) -> tuple:
        raise NotImplementedError()