from sqlalchemy.exc import NoResultFound

from datetime import datetime

from src.data.database.unity_of_work import UnityOfWork
from src.exceptions.exceptions import (
    EntityDoesNotExistsError,
    ServiceError,
)

from src.entity.refresh_token_entity import RefreshTokenEntity
from src.interfaces.domain.interface_refresh_token_domain import IRefreshTokenDomain
from src.interfaces.infrastructure.interface_refresh_token_repository import IRefreshTokenRepository


class RefreshTokenDomain(IRefreshTokenDomain):


    def __init__(self, repository: IRefreshTokenRepository):
        self.__repository = repository

    def attach_uow(self, uow: UnityOfWork):
        self.__repository.uow = uow

    def create_refresh_token(self, token: str, user_id: int, expires_at: datetime) -> RefreshTokenEntity:
        try:
            return self.__repository.create_refresh_token(token, user_id, expires_at)
        except Exception as e:
            raise ServiceError() from e
    
    def get_refresh_token(self, token: str) -> RefreshTokenEntity:
        try:
            return self.__repository.get_refresh_token(token)
        except NoResultFound as e:
            raise EntityDoesNotExistsError('Token não encontrado.') from e
        except Exception as e:
            raise ServiceError() from e
    
    def revoke_refresh_token(self, token_id: int) -> None:
        try:
            return self.__repository.revoke_refresh_token(token_id)
        except NoResultFound as e:
            raise EntityDoesNotExistsError('Token não encontrado') from e
        except Exception as e:
            raise ServiceError() from e