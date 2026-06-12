from fastapi import APIRouter
from app.api.route import (
    auth
)

master_router = APIRouter()

# register all routes
master_router.include_router(auth.router)