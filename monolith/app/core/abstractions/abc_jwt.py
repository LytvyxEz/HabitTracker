from abc import ABC, abstractmethod
from pydantic import EmailStr
from typing import Any

class AbcJWT(ABC):
    @staticmethod
    @abstractmethod
    def encode_jwt(email: EmailStr) -> str:
        raise NotImplementedError()
    
    @staticmethod
    @abstractmethod
    def decode_jwt(token: str) -> Any:
        raise NotImplementedError()
        
    
    @classmethod
    @abstractmethod
    def create_tokens(cls, email: EmailStr) -> tuple:
        raise NotImplementedError()