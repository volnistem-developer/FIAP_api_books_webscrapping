from fastapi import APIRouter, HTTPException

from src.api.config.dependency_injection_config import services
from src.dtos.refresh_token_dto import RefreshTokenRequestDTO
from src.dtos.token_dto import TokenDTO
from src.dtos.user_dto import UserLoginDTO


router = APIRouter(prefix="/api/v1/auth", tags=["Authorization"])

@router.post("/login", response_model=TokenDTO)
def login(user: UserLoginDTO):

    service, uow = services.auth_service()

    with uow:
        return service.create_user_token(username=user.username, password=user.password)


@router.post("/refresh", response_model=TokenDTO)
def refresh(data: RefreshTokenRequestDTO):

    service, uow = services.auth_service()

    with uow:
        return service.update_refresh_token(data.refresh_token)
