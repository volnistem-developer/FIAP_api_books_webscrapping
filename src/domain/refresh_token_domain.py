from sqlalchemy.exc import NoResultFound

from datetime import datetime

from src.domain.exceptions import (
    AppException,
    InfraException,
    NotFoundException,
)

from src.entity.refresh_token_entity import RefreshTokenEntity
from src.interfaces.domain.interface_refresh_token_domain import IRefreshTokenDomain
from src.interfaces.infrastructure.interface_refresh_token_repository import IRefreshTokenRepository


class RefreshTokenDomain(IRefreshTokenDomain):
    def __init__(self, repository: IRefreshTokenRepository):
        self.__repository = repository
        self.__validation: list[AppException] = []

    @property
    def validation(self) -> list[AppException]:
        return self.__validation

    def create_refresh_token(self, token: str, user_id: int, expires_at: datetime) -> RefreshTokenEntity | None:
        response = None

        try:
            response = self.__repository.create_refresh_token(token, user_id, expires_at)
            
        except Exception:
            self.add_validation(InfraException("Erro ao acessar a base de dados"))

        return response
    
    def get_refresh_token(self, token: str) -> RefreshTokenEntity:
        retorno = None

        try:
            retorno = self.__repository.get_refresh_token(token)

        except NoResultFound:
            self.add_validation(NotFoundException("Registro não encontrado"))
        except Exception:
            self.add_validation(InfraException("Erro ao acessar a base de dados"))
        
        return retorno
    
    def revoke_refresh_token(self, token_id: int) -> None:
        try:
            self.__repository.revoke_refresh_token(token_id)
        except Exception:
            self.add_validation(InfraException("Erro ao acessar a base de dados")) 
    
    def add_validation(self, ex):
        self.__validation.append(ex)