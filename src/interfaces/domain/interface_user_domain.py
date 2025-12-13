from abc import abstractmethod
from src.entity.user_entity import UserEntity
from src.interfaces.domain.interface_base_domain import IBaseDomain


class IUserDomain(IBaseDomain):

    @abstractmethod
    def list(self) -> list[UserEntity]: pass

    @abstractmethod
    def get(self, id: int) -> UserEntity: pass

    @abstractmethod
    def get_by_username(self, username: str) -> UserEntity: pass

    @abstractmethod
    def insert(self, entidade: UserEntity) -> UserEntity | None: pass

    @abstractmethod
    def delete(self, id: int) -> None: pass

    @abstractmethod
    def update(self, id: int, name: str) -> UserEntity: pass