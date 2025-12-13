from datetime import datetime
from typing import Optional
from src.domain.exceptions import AppException
from src.entity.refresh_token_entity import RefreshTokenEntity
from src.interfaces.application.interface_application_refresh_token import IRefreshTokenApplication
from src.interfaces.domain.interface_refresh_token_domain import IRefreshTokenDomain


class RefreshTokenApplication(IRefreshTokenApplication):
    def __init__(self, domain: IRefreshTokenDomain) -> None:
        self.__domain = domain
    
    @property
    def validation(self) -> list[AppException]:
        return self.__domain.validation

    def create_refresh_token(self, token: str, user_id: int, expires_at: datetime) -> RefreshTokenEntity | None:
        return self.__domain.create_refresh_token(token, user_id, expires_at)
    
    def get_refresh_token(self, token: str) -> Optional[RefreshTokenEntity]:
        return self.__domain.get_refresh_token(token)
    
    def revoke_refresh_token(self, token_id: int) -> None:
        self.__domain.revoke_refresh_token(token_id)