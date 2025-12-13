from abc import abstractmethod

from src.entity.user_entity import UserEntity
from src.interfaces.application.interface_application_base import IApplicationBase


class IUserApplication(IApplicationBase):

    @abstractmethod
    def list_all(self) -> list[UserEntity]: pass

    @abstractmethod
    def get_by_id(self, id: int) -> UserEntity: pass

    @abstractmethod
    def get_by_username(self, username: str) -> UserEntity: pass

    @abstractmethod
    def insert_user(self, entidade: UserEntity) -> UserEntity | None: pass

    @abstractmethod
    def delete_user(self, id:int) -> None: pass

    @abstractmethod
    def update_user(self, id:int, name:str) -> UserEntity: pass