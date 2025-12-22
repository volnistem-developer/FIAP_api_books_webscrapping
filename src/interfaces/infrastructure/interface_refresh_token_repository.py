from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional

from src.data.database.unity_of_work import UnityOfWork
from src.entity.refresh_token_entity import RefreshTokenEntity



class IRefreshTokenRepository(ABC):

    @abstractmethod
    def __init__(self, uow: UnityOfWork):
        """
        Inicializa o repositório com uma Unit of Work.
        """
        pass

    @abstractmethod
    def create_refresh_token(self, token: str, user_id: int, expires_at: datetime) -> RefreshTokenEntity:
        """
        Persiste um novo refresh token.
        Commit é responsabilidade da Application/UoW.
        """
        pass

    @abstractmethod
    def get_refresh_token(self, token: str) -> Optional[RefreshTokenEntity]:
        """
        Retorna um refresh token válido (não revogado)
        ou None se não existir.
        """
        pass

    @abstractmethod
    def revoke_refresh_token(self, token_id: int) -> None:
        """
        Revoga um refresh token específico pelo ID.
        """
        pass

    @abstractmethod
    def revoke_all_user_refresh_tokens(self, user_id: int) -> None:
        """
        Revoga todos os refresh tokens de um usuário.
        """
        pass