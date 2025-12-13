from abc import abstractmethod
from datetime import datetime
from src.entity.refresh_token_entity import RefreshTokenEntity
from src.interfaces.domain.interface_base_domain import IBaseDomain


class IRefreshTokenDomain(IBaseDomain):

    @abstractmethod
    def create_refresh_token(self, token: str, user_id: int, expires_at: datetime) -> RefreshTokenEntity | None: pass

    @abstractmethod
    def get_refresh_token(self, token: str) -> RefreshTokenEntity: pass

    @abstractmethod
    def revoke_refresh_token(self, token_id: int) -> None: pass