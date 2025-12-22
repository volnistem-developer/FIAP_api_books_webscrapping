from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional
from src.data.database.unity_of_work import UnityOfWork
from src.entity.refresh_token_entity import RefreshTokenEntity


class IRefreshTokenDomain(ABC):

    @abstractmethod
    def attach_uow(self, uow: UnityOfWork) -> None:
        """
        Associa a Unit of Work ao domínio.
        """
        pass

    @abstractmethod
    def create_refresh_token(self, token: str, user_id: int, expires_at: datetime) -> RefreshTokenEntity:
        """
        Cria um novo refresh token para um usuário.
        """
        pass

    @abstractmethod
    def get_refresh_token(self, token: str) -> Optional[RefreshTokenEntity]:
        """
        Retorna um refresh token válido ou None se não existir.
        """
        pass

    @abstractmethod
    def revoke_refresh_token(self, token_id: int) -> None:
        """
        Revoga um refresh token pelo ID.
        """
        pass