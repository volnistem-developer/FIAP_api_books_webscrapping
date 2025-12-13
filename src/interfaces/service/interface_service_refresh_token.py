from abc import abstractmethod
from src.dtos.token_dto import TokenDTO
from src.interfaces.service.interface_service_base import IServiceBase


class IServiceRefreshToken(IServiceBase):

    @abstractmethod
    def create_user_token(self, username: str, password:str) -> TokenDTO: pass

    @abstractmethod
    def update_refresh_token(self, refresh_token: str) -> TokenDTO: pass

