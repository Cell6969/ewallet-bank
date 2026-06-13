from typing import Annotated
from fastapi import BackgroundTasks, Depends, HTTPException, status
from sqlalchemy.ext.asyncio  import AsyncSession
from app.database.sql import get_db
from app.service.user import UserService
from app.service.wallet import WalletService
from app.service.topup import TopupService

# Inject Session
SessionDep = Annotated[AsyncSession,Depends(get_db)]

# Inject Service
def get_user_service(session:SessionDep):
    return UserService(
        session=session, 
        wallet_service=WalletService(session=session)
    )

def get_wallet_service(session:SessionDep):
    return WalletService(session=session)

def get_topup_service(session:SessionDep):
    return TopupService(
        session=session,
        wallet_service=WalletService(session=session)
    )

# Initialize Service
UserServiceDep = Annotated[UserService, Depends(get_user_service)]
WalletServiceDep = Annotated[WalletService, Depends(get_wallet_service)]
TopupServiceDep = Annotated[TopupService, Depends(get_topup_service)]
