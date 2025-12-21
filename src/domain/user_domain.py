from sqlalchemy.exc import IntegrityError, NoResultFound

from src.data.database.unity_of_work import UnityOfWork
from src.exceptions.exceptions import (
    BookScrapingApiError,
    EntityDoesNotExistsError,
    IntegrityError,
    ServiceError
)

from src.entity.user_entity import UserEntity
from src.interfaces.domain.interface_user_domain import IUserDomain
from src.interfaces.infrastructure.interface_user_repository import IUserRepository

class UserDomain(IUserDomain):

    def __init__(self, repository: IUserRepository):
        self.__repository = repository

    def attach_uow(self, uow: UnityOfWork):
        self.__repository.uow = uow


    def list(self) -> list[UserEntity]:
        try:
            return self.__repository.list()
        except Exception as e:
            raise ServiceError() from e
    
    def get(self, id: int) -> UserEntity:
        try:
            return self.__repository.get(id)
        except NoResultFound as e:
            raise EntityDoesNotExistsError("Usuário não encontrado") from e
        except Exception as e:
            raise ServiceError() from e
        
    
    def get_by_username(self, username: str) -> UserEntity:
        try:
            return self.__repository.get_by_username(username)
        except NoResultFound as e:
            raise EntityDoesNotExistsError("Usuário não encontrado") from e
        except Exception as e:
            raise ServiceError() from e

    def insert(self, entidade: UserEntity) -> UserEntity:
        try:
            return self.__repository.insert(entidade)

        except IntegrityError as e:
            msg = str(e.orig).lower()

            if "email" in msg:
                raise ServiceError("Esse e-mail já existe na base de dados.") from e
            if "username" in msg:
                raise ServiceError("Esse usuário já existe na base de dados.") from e

            raise ServiceError() from e

        except Exception as e:
            raise ServiceError() from e
    
    def delete(self, id: int) -> None:
        try:
            self.__repository.delete(id)
        except NoResultFound as e:
            raise EntityDoesNotExistsError("Usuário não encontrado") from e
        except Exception as e:
            raise ServiceError() from e

    def update(self, id: int, name: str, username: str, email: str) -> UserEntity:
        try:
            return self.__repository.update(id, name, username, email)
        except NoResultFound as e:
            raise EntityDoesNotExistsError("Usuário não encontrado") from e
        except Exception as e:
            raise ServiceError() from e
