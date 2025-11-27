from sqlalchemy.exc import IntegrityError, NoResultFound

from src.dominio.dominio_base import DominioBase
from src.dominio.exceptions import (
    BusinessException,
    ConflictException,
    InfraException,
    NotFoundException,
)
from src.entidades.role_entity import RoleEntity
from src.interfaces.dominio.retorno_validacao_interface import IRetornoValidacao
from src.interfaces.infraestrutura.repositorio_role_interface import IRepositorioRole


class DominioRole(DominioBase):
    def __init__(
        self, repositorio: IRepositorioRole, retorno_validacao: IRetornoValidacao
    ) -> None:
        super().__init__(retorno_validacao)
        self.__repositorio = repositorio

    def list(self) -> list[RoleEntity]:
        retorno: list[RoleEntity] = []

        try:
            retorno = self.__repositorio.list()

        except BusinessException as ex:
            self.retorno_validacao.add_exception(ex)

        except Exception:
            self.retorno_validacao.add_exception(
                InfraException("Erro ao acessar a base de dados")
            )

        return retorno
    
    def get(self, id: int) -> RoleEntity:
        retorno = None

        try:
            retorno = self.__repositorio.get(id)

        except NoResultFound:
            self.retorno_validacao.add_exception(
                NotFoundException("Registro não encontrado")
            )
        except Exception:
            self.retorno_validacao.add_exception(
                InfraException("Erro ao acessar a base de dados")
            )
        
        return retorno

    def insert(self, entidade: RoleEntity) -> RoleEntity | None:
        retorno = None

        try:
            retorno = self.__repositorio.insert(entidade)

        except IntegrityError:
            self.retorno_validacao.add_exception(
                ConflictException("Já existe um cargo com esse nome")
            )

        except Exception:
            self.retorno_validacao.add_exception(
                InfraException("Erro ao acessar a base de dados")
            )

        return retorno
    
    def delete(self, id: int) -> None:

        try:
            self.__repositorio.delete(id)

        except NoResultFound:
            self.retorno_validacao.add_exception(
                NotFoundException("Registro não encontrado")
            )
        except Exception:
            self.retorno_validacao.add_exception(
                InfraException("Erro ao acessar a base de dados")
            )

    def update(self, id: int, name: str) -> RoleEntity:
        retorno = None

        try:
            retorno = self.__repositorio.update(id, name)
        except NoResultFound:
            self.retorno_validacao.add_exception(
                NotFoundException("Registro não encontrado")
            )
        except Exception as ex:
            print(ex)
            self.retorno_validacao.add_exception(
                InfraException("Erro ao acessar a base de dados")
            )

        return retorno