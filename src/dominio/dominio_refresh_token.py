from sqlalchemy.exc import NoResultFound

from datetime import datetime
from src.dominio.dominio_base import DominioBase

from src.dominio.exceptions import (
    BusinessException,
    ConflictException,
    InfraException,
    NotFoundException,
)

from src.entidades.refresh_token_entity import RefreshTokenEntity
from src.infraestrutura.repositorio_refresh_token import RepositorioRefreshToken
from src.interfaces.dominio.retorno_validacao_interface import IRetornoValidacao


class DominioRefreshToken(DominioBase):
    def __init__(
        self, retorno_validacao: IRetornoValidacao
    ) -> None:
        super().__init__(retorno_validacao)
        self.__repositorio = RepositorioRefreshToken()

    def create_refresh_token(self, token: str, user_id: int, expires_at: datetime):
        try:
            retorno = self.__repositorio.create_refresh_token(token, user_id, expires_at)
        except Exception:
            self.retorno_validacao.add_exception(
                InfraException("Erro ao acessar a base de dados")
            )

        return retorno
    
    def get_refresh_token(self, token: str) -> RefreshTokenEntity:
        retorno = None

        try:
            retorno = self.__repositorio.get_refresh_token(token)

        except NoResultFound:
            self.retorno_validacao.add_exception(
                NotFoundException("Registro não encontrado")
            )
        except Exception:
            self.retorno_validacao.add_exception(
                InfraException("Erro ao acessar a base de dados")
            )
        
        return retorno
    
    def revoke_refresh_token(self, token_id: int) -> None:
        try:
            self.__repositorio.revoke_refresh_token(token_id)
        except Exception:
            self.retorno_validacao.add_exception(
                InfraException("Erro ao acessar a base de dados")
            ) 