from fastapi import FastAPI, APIRouter

from typing import List

from .api.auth import auth_router
from .db import lifespan

class App:
    def __init__(self, routers: List[APIRouter] = None, **kwargs) -> None:
        self.routers = routers
        
        self.kwargs = kwargs


    def __call__(self) -> FastAPI:
        """Create FastAPI instance"""
        
        app = FastAPI(**self.kwargs)

        if self.routers:
            for router in self.routers:
                app.include_router(router)

        return app


app = App(routers=[auth_router, ], lifespan=lifespan, title='HabitTracker')

