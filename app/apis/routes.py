from fastapi import APIRouter

from app.apis.endpoints.user import router as user_router

routers = APIRouter()
routers.include_router(user_router)
