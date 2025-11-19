from app.core.abstractions import AbcUserDao


class UserDAO(AbcUserDao):
    async def get_by_email():
        ...

    async def create_user():
        ...

    async def save_refresh_token():
        ...

    async def delete_refresh_token():
        ...

    async def get_refresh_token():
        ...
        
        
user_dao_manager = UserDAO()