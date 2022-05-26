from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from app.services.user_service import UserService
from app.core.container import Container
from app.schema.user import User

router = APIRouter(
    prefix='/user',
    tags=['user'],
)

@router.get('/{id}', response_model=User)
@inject
async def get_user(
    id: int,
    service: UserService = Depends(Provide[Container.user_service]),
):
    return service.get_by_id(id)
