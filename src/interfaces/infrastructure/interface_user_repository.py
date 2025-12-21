from abc import ABC, abstractmethod

from src.entity.user_entity import UserEntity


class IUserRepository(ABC):
    
    @abstractmethod
    def list(self) -> list[UserEntity]: pass

    @abstractmethod
    def get(self, id: int) -> UserEntity: pass

    def get_by_username(self, username: str) -> UserEntity: pass

    @abstractmethod
    def insert(self, entity: UserEntity) -> UserEntity: pass

    @abstractmethod
    def delete(self, id: int) -> None: pass

    @abstractmethod
    def update(self, id: int, name: str, username: str, email: str) -> UserEntity: pass
