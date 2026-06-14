from fastapi import APIRouter, Request, Depends
from app.api.schema.transaction import TopupRequest, TopupResponse
from app.api.dependency import TransactionServiceDep
from app.helper.api import ApiResponse
from app.core.security import get_auth_user


router = APIRouter(prefix='/tx', tags=['Transaction'])

@router.post('/topup', response_model=ApiResponse[TopupResponse])
async def topup(
        body:TopupRequest,
        transaction_service: TransactionServiceDep,
        user:dict=Depends(get_auth_user),
    ):
    result = await transaction_service.topup(user_id=user['id'],data=body)
    return ApiResponse.success("success topup wallet", data=result)