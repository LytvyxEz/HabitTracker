from sqlalchemy import select

from ..db.models import User
from ..api.auth.schemas import RegisterSchema
from app.core.abstractions import AbcUserDAO

class UserDAO(AbcUserDAO):
    
    
    async def get_by_email(self, email: str):
        user = await self.db.execute(select(User).where(User.email == email)) 
        return user.scalar_one_or_none()
        
    async def get_by_id(self, user_id: int):
        user = await self.db.execute(select(User).where(User.id == user_id))    
        return user.scalar_one_or_none()
    
    
    async def create_user(self, user: RegisterSchema):
        user = User(
            email=user.email,
            username=user.username,
            password=user.password
            )
        self.db.add(user)
        
        await self.db.commit()
        await self.db.refresh(user)
        
        return user
