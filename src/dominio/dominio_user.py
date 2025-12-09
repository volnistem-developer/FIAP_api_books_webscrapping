from sqlalchemy.exc import IntegrityError, NoResultFound

from src.dominio.dominio_base import DominioBase
from src.dominio.exceptions import (
    BusinessException,
    ConflictException,
    InfraException,
    NotFoundException,
)
from src.entidades.user_entity import UserEntity
from src.infraestrutura.repositorio_user import RepositorioUser
from src.interfaces.dominio.retorno_validacao_interface import IRetornoValidacao

class DominioUser(DominioBase):
    def __init__(
        self, retorno_validacao: IRetornoValidacao
    ) -> None:
        super().__init__(retorno_validacao)
        self.__repositorio = RepositorioUser()

    def list(self) -> list[UserEntity]:
        retorno: list[UserEntity] = []

        try:
            retorno = self.__repositorio.list()

        except BusinessException as ex:
            self.retorno_validacao.add_exception(ex)

        except Exception as ex:
            self.retorno_validacao.add_exception(
                InfraException(str(ex))
            )

        return retorno
    
    def get(self, id: int) -> UserEntity:
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
    
    def get_by_username(self, username: str) -> UserEntity:
        retorno = None

        try: 
            retorno = self.__repositorio.get_by_username(username)

        except NoResultFound:
            self.retorno_validacao.add_exception(
                NotFoundException("Registro não encontrado")
            )
        except Exception:
            self.retorno_validacao.add_exception(
                InfraException("Erro ao acessar a base de dados")
            )
        
        return retorno

    def insert(self, entidade: UserEntity) -> UserEntity | None:
        retorno = None

        try:
            retorno = self.__repositorio.insert(entidade)

        except IntegrityError as e:
            msg = str(e.orig).lower()

            if "email" in msg: 
                self.retorno_validacao.add_exception(
                    ConflictException("Já existe um usuário com esse email")
                )
            elif "username" in msg:
                self.retorno_validacao.add_exception(
                    ConflictException("Já existe um usuário com esse username")
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

    def update(self, id: int, name: str) -> UserEntity:
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