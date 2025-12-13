from fastapi import APIRouter, HTTPException

from src.api.configuration.dependency_injection_config import services
from src.dtos.refresh_token_dto import RefreshTokenRequestDTO
from src.dtos.token_dto import TokenDTO
from src.dtos.user_dto import UserLoginDTO


router = APIRouter(prefix="/api/v1/auth", tags=["Authorization"])

@router.post("/login", response_model=TokenDTO)
def login(user: UserLoginDTO):

    retorno = services.refresh_service.create_user_token(username=user.username, password=user.password)

    if len(services.refresh_service.validation) > 0:   
        ex = services.refresh_service.validation[0]   

        raise HTTPException(status_code=ex.status_code, detail=ex.message)

    return retorno

@router.post("/refresh", response_model=TokenDTO)
def refresh(data: RefreshTokenRequestDTO):

    retorno = services.refresh_service.update_refresh_token(data.refresh_token)

    if len(services.refresh_service.validation) > 0:   
        ex = services.refresh_service.validation[0]   

        raise HTTPException(status_code=ex.status_code, detail=ex.message)

    return retorno