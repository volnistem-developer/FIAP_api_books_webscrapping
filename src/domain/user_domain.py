from sqlalchemy.exc import IntegrityError, NoResultFound

from src.domain.exceptions import (
    AppException,
    BusinessException,
    ConflictException,
    InfraException,
    NotFoundException,
)

from src.entity.user_entity import UserEntity
from src.interfaces.domain.interface_user_domain import IUserDomain
from src.interfaces.infrastructure.interface_user_repository import IUserRepository

class UserDomain(IUserDomain):

    def __init__(self, repository: IUserRepository):
        self.__repository = repository
        self.__validation: list[AppException] = []

    @property
    def validation(self) -> list[AppException]:
        return self.__validation


    def list(self) -> list[UserEntity]:
        response: list[UserEntity] = []

        try:
            response = self.__repository.list()

        except BusinessException as ex:
            self.add_validation(ex)

        except Exception as ex:
            self.add_validation(InfraException(str(ex)))

        return response
    
    def get(self, id: int) -> UserEntity:
        response = None

        try:
            response = self.__repository.get(id)

        except NoResultFound:
            self.add_validation(NotFoundException("Registro não encontrado"))
        except Exception:
            self.add_validation(InfraException("Erro ao acessar a base de dados"))
        
        return response
    
    def get_by_username(self, username: str) -> UserEntity:
        response = None

        try: 
            response = self.__repository.get_by_username(username)

        except NoResultFound:
            self.add_validation(NotFoundException("Registro não encontrado"))
        except Exception:
            self.add_validation(InfraException("Erro ao acessar a base de dados"))
        
        return response

    def insert(self, entidade: UserEntity) -> UserEntity | None:
        response = None

        try:
            response = self.__repository.insert(entidade)

        except IntegrityError as e:
            msg = str(e.orig).lower()

            if "email" in msg: 
                self.add_validation(ConflictException("Já existe um usuário com esse email"))
            elif "username" in msg:
                self.add_validation(ConflictException("Já existe um usuário com esse username"))

        except Exception:
            self.add_validation(InfraException("Erro ao acessar a base de dados"))

        return response
    
    def delete(self, id: int) -> None:

        try:
            self.__repository.delete(id)

        except NoResultFound:
            self.add_validation(NotFoundException("Registro não encontrado"))
        except Exception:
            self.add_validation(InfraException("Erro ao acessar a base de dados"))

    def update(self, id: int, name: str) -> UserEntity:
        response = None

        try:
            response = self.__repository.update(id, name)
        except NoResultFound:
            self.add_validation(NotFoundException("Registro não encontrado"))
        except Exception:
            self.add_validation(InfraException("Erro ao acessar a base de dados"))

        return response

    def add_validation(self, ex):
        self.__validation.append(ex)