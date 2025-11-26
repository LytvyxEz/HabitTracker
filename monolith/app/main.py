from fastapi import FastAPI, APIRouter

from typing import Tuple

from .db import lifespan

class App:
    def __init__(self, **kwargs) -> None:        
        self.kwargs = kwargs


    def get_routers(self) -> Tuple[APIRouter, ...]:
        """Import routers to avoid circular imports"""
        from .api.auth import auth_router
        from .api.user import user_router
        
        return auth_router, user_router
        
        
    def include_routers(self, app: FastAPI) -> None:
        """Includes all imported routers to app"""
        
        routers = self.get_routers()
        
        if routers:
            for router in routers:
                app.include_router(router)

        
    def create(self) -> FastAPI:
        """Creates a FastAPI instance"""
        
        app = FastAPI(**self.kwargs)
        self.include_routers(app)

        return app
        
        
    def __call__(self) -> FastAPI:
        """Using call to create a FastAPI instance"""
        return self.create()


app = App(lifespan=lifespan, title='HabitTracker')

