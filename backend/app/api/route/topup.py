from fastapi import APIRouter, Request, Depends
from app.api.schema.topup import TopupRequest
from app.api.dependency import TopupServiceDep
from app.helper.api import ApiResponse
from app.core.security import get_auth_user


router = APIRouter(prefix='/topup', tags=['topup'])

@router.post('')
async def add_balance(
        body:TopupRequest,
        topup_service: TopupServiceDep,
        user:dict=Depends(get_auth_user),
    ):
    result = await topup_service.topup(user_id=user['id'],data=body)
    return result