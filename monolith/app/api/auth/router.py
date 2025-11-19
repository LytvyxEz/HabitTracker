from fastapi import APIRouter

router = APIRouter(prefix='/auth')



@router.post('/register')
async def register():
    ...


@router.post('/login')
async def login():
    ...


@router.post('/refresh')
async def refresh():
    ...
    
    
@router.post('/logout')
async def logout():
    ...