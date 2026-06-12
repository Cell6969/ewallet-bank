from fastapi import APIRouter
from app.api.schema.auth import *
from app.api.dependency import UserServiceDep
from app.helper.api import ApiResponse

router = APIRouter(prefix='/auth', tags=['auth'])

@router.post('/signup', response_model=ApiResponse[UserResponse])
async def register(
    body: RegisterRequest,
    service: UserServiceDep
):
    user = await service.register(body)
    return ApiResponse.success("Success register user", user)