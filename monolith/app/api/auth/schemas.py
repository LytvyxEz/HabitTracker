from pydantic import BaseModel, EmailStr, field_validator, ValidationInfo
from fastapi import HTTPException

    
class RegisterSchema(BaseModel):
    email: EmailStr
    username: str
    password: str
    repeat_password: str
    
    
    @field_validator('password')
    def validate_password(cls, value: str):
        special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/~`\"\\"
        
        if len(value) < 8:
            raise ValueError("Password must be at least 8 symbols in lenght")

        if not any(char.isupper() for char in value):
            raise ValueError("Password must have at least one uppercase letter")

        if not any(char.islower() for char in value):
            raise ValueError("Password must have at least one lowercase letter")

        if not any(char.isdigit() for char in value):
            raise ValueError("Password must have at least one digit")

        if not any(char in special_chars for char in value):
            raise ValueError("Password must have at least one special symbol")

        return value
        
    @field_validator('repeat_password')
    def repeat_password_validation(cls, v: str, info: ValidationInfo):
        if 'password' in info.data and v != info.data['password']:
            raise ValueError('Passwords do not match')
        return v
    
    

class LoginSchema(BaseModel):
    email: EmailStr
    username: str
    password: str

    


class TokenResponse(BaseModel):
    
    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
    