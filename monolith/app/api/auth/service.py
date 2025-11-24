from fastapi import HTTPException, Depends, Cookie

from typing import Optional

from ...core.abstractions import AbcAuthService
from ..auth.schemas import UserResponse, RegisterSchema, LoginSchema


class AuthService(AbcAuthService):    
    
    async def create_tokens(self, user: UserResponse):
        access, refresh = self.jwt_manager.create_tokens(user)
        refresh_payload = self.jwt_manager.decode_jwt(refresh)
        
        sid = refresh_payload["sid"]
        ttl = refresh_payload["exp"] - refresh_payload["iat"]
        
        await self.refresh_repo.save(sid, user.id, ttl_second=ttl)
        
        return access, refresh
    
    
    async def refresh_token_check(self, refresh_token: str):
        # payload = self.jwt_manager.decode_jwt(refresh_token)
        # if payload["typ"] != "refresh":
        #     raise HTTPException(401, "Wrong token type")
        
        # sid = payload["sid"]
        # stored_user_id = await self.refresh_repo.exists(sid)
        
        # if not stored_user_id:
        #     raise HTTPException(401, "Refresh token expired or revoked")
        
        # if str(stored_user_id) != str(payload["sub"]):
        #     raise HTTPException(401, "Token user mismatch")
        
        # await self.refresh_repo.delete(sid)
        
        # user = await self.user_dao.get_by_id(int(payload["sub"]))
        # access, refresh = await self.create_tokens(user)
        
        # return {
        #     "access": access,
        #     "refresh": refresh
        # }
        ... #TODO
        
    
    async def create_user(self, user_data: RegisterSchema) -> UserResponse: 
        hashed_password = await self.hash_manager.hash_password(user_data.password)  
        
        user = await self.user_dao.create_user(
            username=user_data.username,
            email=user_data.email,
            password=hashed_password
        )
        
        return UserResponse(
            id=user.id,
            email=user.email,
            username=user.username
        )


    async def login_user(self, user_data: LoginSchema) -> tuple:
        user = await self.user_dao.login_user(user_data)
        
        if not await self.hash_manager.check_password(user_data.password, user.password):
            from ...core.abstractions import InvalidCredentials
            raise InvalidCredentials('Invalid password')
        
        access_token = (await self.create_tokens(user))[0]
        


        return user, access_token
    
    async def logout_user(self, user: UserResponse, sid: str) -> None:
        await self.refresh_repo.delete(sid)
    
    
