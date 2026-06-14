from fastapi import APIRouter
from app.api.route import (
    auth,
    transaction
)


master_router = APIRouter()

# register all routes
master_router.include_router(auth.router)
master_router.include_router(transaction.router)