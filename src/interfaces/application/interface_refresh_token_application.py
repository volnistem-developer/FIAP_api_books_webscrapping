from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional
from src.entity.refresh_token_entity import RefreshTokenEntity


class IRefreshTokenApplication(ABC):

    @abstractmethod
    def create_refresh_token(
        self,
        token: str,
        user_id: int,
        expires_at: datetime
    ) -> RefreshTokenEntity:
        """
        Cria e persiste um refresh token para um usuário.
        """
        pass

    @abstractmethod
    def get_refresh_token(
        self,
        token: str
    ) -> Optional[RefreshTokenEntity]:
        """
        Retorna um refresh token válido ou None se não existir.
        """
        pass

    @abstractmethod
    def revoke_refresh_token(
        self,
        token_id: int
    ) -> None:
        """
        Revoga um refresh token pelo ID.
        """
        pass