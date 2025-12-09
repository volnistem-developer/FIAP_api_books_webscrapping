from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from src.api.service.auth_service import ServiceAuth
from src.dtos.refresh_token_dto import RefreshTokenRequestDTO
from src.dtos.token_dto import TokenDTO
from src.dtos.user_dto import UserLoginDTO


router = APIRouter(prefix="/api/v1/auth", tags=["Authorization"])

@router.post("/login", response_model=TokenDTO)
def login(user: UserLoginDTO):
    service = ServiceAuth()

    retorno = service.create_user_token(username=user.username, password=user.password)

    if service.has_exceptions():
        erros = service.get_exceptions()

        erro = erros[0]

        raise HTTPException(status_code=erro.status_code, detail=erro.message)

    return retorno

@router.post("/refresh", response_model=TokenDTO)
def refresh(data: RefreshTokenRequestDTO):
    service = ServiceAuth()

    retorno = service.update_refresh_token(data.refresh_token)

    if service.has_exceptions():
        erros = service.get_exceptions()

        erro = erros[0]

        raise HTTPException(status_code=erro.status_code, detail=erro.message)

    return retorno