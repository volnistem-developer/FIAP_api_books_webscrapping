from abc import ABC, abstractmethod
from src.dtos.token_dto import TokenDTO


class IServiceRefreshToken(ABC):

    @abstractmethod
    def create_user_token(self, username: str, password:str) -> TokenDTO: pass

    @abstractmethod
    def update_refresh_token(self, refresh_token: str) -> TokenDTO: pass

