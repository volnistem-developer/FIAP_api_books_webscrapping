from src.data.database.unity_of_work import UnityOfWork
from src.entity.user_entity import UserEntity
from src.interfaces.application.interface_user_application import IUserApplication
from src.interfaces.domain.interface_user_domain import IUserDomain


class UserApplication(IUserApplication):

    def __init__(self, domain: IUserDomain) -> None:
        self.__domain = domain

    def list_all(self) -> list[UserEntity]:
        with UnityOfWork() as uow:
            self.__domain.attach_uow(uow)
            return self.__domain.list()

    def get_by_id(self, id: int) -> UserEntity:
        with UnityOfWork() as uow:
            self.__domain.attach_uow(uow)
            return self.__domain.get(id)

    def get_by_username(self, username: str) -> UserEntity:
        with UnityOfWork() as uow:
            self.__domain.attach_uow(uow)
            return self.__domain.get_by_username(username)

    def insert_user(self, entity: UserEntity) -> UserEntity:
        with UnityOfWork() as uow:
            self.__domain.attach_uow(uow)
            created = self.__domain.insert(entity)
            return created

    def delete_user(self, id: int) -> None:
        with UnityOfWork() as uow:
            self.__domain.attach_uow(uow)
            self.__domain.delete(id)

    def update_user(self, id: int, name: str, username: str, email: str) -> UserEntity:
        with UnityOfWork() as uow:
            self.__domain.attach_uow(uow)
            updated = self.__domain.update(id, name, username, email)
            return updated
