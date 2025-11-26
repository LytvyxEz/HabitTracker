from sqlalchemy import select, or_, and_

from ..db.models import User
from ..api.auth.schemas import LoginSchema
from app.core.abstractions import AbcUserDAO


class UserDAO(AbcUserDAO):
    
    
    async def get_by_email(self, email: str):
    
        user = await self.db.execute(select(User).filter(User.email == email)).scalar_one_or_none()
        if not user:
            from app.core.abstractions import UserNotFoundError 
            raise UserNotFoundError(f"User with email '{email}' is not found")
        return user
        
    async def get_by_id(self, user_id: int):
        user = (await self.db.execute(select(User).filter(User.id == user_id))).scalar_one_or_none() 
        if not user:
            from app.core.abstractions import UserNotFoundError
            raise UserNotFoundError('User is not found')
        return user
    
    
    async def create_user(self, email: str, username: str, password: bytes):
        user = {
            'email': email,
            'username': username,
            'password': password
        }
        if (await self.db.execute(select(User).filter(or_(User.email == email, User.username == username)))).scalar_one_or_none():
            from app.core.abstractions import UserAlreadyExistsError
            raise UserAlreadyExistsError('User with this email or username already exists')
        
        new_user = User(**user)
        self.db.add(new_user)
        
        await self.db.commit()
        await self.db.refresh(new_user)
        
        return new_user


    async def login_user(self, user_data: LoginSchema):
        user = (await self.db.execute(
            select(User).filter(
                and_(
                    User.email == user_data.email,
                    User.username == user_data.username
                )
            )
        )).scalar_one_or_none()
        
                
        if not user:
            from app.core.abstractions import UserDoesNotExistsError
            raise UserDoesNotExistsError('User with this email and username does not exists')
        
        return user
        