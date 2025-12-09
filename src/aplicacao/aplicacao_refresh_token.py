from datetime import datetime
from typing import Optional
from src.dominio.dominio_refresh_token import DominioRefreshToken
from src.dominio.dominio_retorno_validacao import DominioRetornoValidacao
from src.entidades.refresh_token_entity import RefreshTokenEntity


class AplicacaoRefreshToken():
    def __init__(self) -> None:
        self.__retorno = DominioRetornoValidacao()
        self.dominio = DominioRefreshToken(retorno_validacao=self.__retorno)

    def create_refresh_token(self, token: str, user_id: int, expires_at: datetime) -> RefreshTokenEntity:
        return self.dominio.create_refresh_token(token, user_id, expires_at)
    
    def get_refresh_token(self, token: str) -> Optional[RefreshTokenEntity]:
        return self.dominio.get_refresh_token(token)
    
    def revoke_refresh_token(self, token_id: int) -> None:
        self.dominio.revoke_refresh_token(token_id)