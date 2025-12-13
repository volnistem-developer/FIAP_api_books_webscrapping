from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional

from src.entity.refresh_token_entity import RefreshTokenEntity


class IRefreshTokenRepository(ABC):

    @abstractmethod
    def create_refresh_token(self, token: str, user_id: int, expires_at: datetime) -> RefreshTokenEntity: pass

    @abstractmethod
    def get_refresh_token(self, token: str) -> Optional[RefreshTokenEntity]: pass

    @abstractmethod
    def revoke_refresh_token(self, token_id: int) -> None: pass

    @abstractmethod
    def revoke_all_user_refresh_tokens(self, user_id: int) -> None: pass