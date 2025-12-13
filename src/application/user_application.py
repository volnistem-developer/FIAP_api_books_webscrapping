from src.domain.exceptions import AppException
from src.entity.user_entity import UserEntity
from src.interfaces.application.interface_application_user import IUserApplication
from src.interfaces.domain.interface_user_domain import IUserDomain


class UserApplication(IUserApplication):
    def __init__(self, domain: IUserDomain) -> None:
        self.__domain = domain
    
    @property
    def validation(self) -> list[AppException]:
        return self.__domain.validation

    def list_all(self) -> list[UserEntity]:
        return self.__domain.list()
    
    def get_by_id(self, id: int) -> UserEntity:
        return self.__domain.get(id)
    
    def get_by_username(self, username: str) -> UserEntity:
        return self.__domain.get_by_username(username)

    def insert_user(self, entidade: UserEntity) -> UserEntity | None:
        return self.__domain.insert(entidade)
    
    def delete_user(self, id:int) -> None:
        self.__domain.delete(id)

    def update_user(self, id:int, name:str) -> UserEntity:
        return self.__domain.update(id, name)
