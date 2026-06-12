from fastapi import APIRouter, Request, Depends
from app.api.schema.auth import *
from app.api.dependency import UserServiceDep
from app.helper.api import ApiResponse
from app.core.security import get_auth_user

router = APIRouter(prefix='/auth', tags=['auth'])

@router.post('/signup', 
    status_code=201,
    response_model=ApiResponse[UserResponse]
)
async def register(
    body: RegisterRequest,
    service: UserServiceDep
):
    user = await service.register(body)
    return ApiResponse.created("Success register user", user)

@router.post('/login', response_model=ApiResponse[UserResponse])
async def login(
    body: LoginRequest,
    service: UserServiceDep
):
    user = await service.login(body)
    return ApiResponse.success("Success login user", user)

@router.get('/profile')
async def profile(user:dict = Depends(get_auth_user)):
    return user