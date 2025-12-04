from abc import ABC, abstractmethod

from src.entidades.user_entity import UserEntity


class IRepositorioUser(ABC):
    @abstractmethod
    def list(self) -> list[UserEntity]: pass

    @abstractmethod
    def get(self, id: int) -> UserEntity: pass

    @abstractmethod
    def insert(self, entity: UserEntity) -> UserEntity: pass

    @abstractmethod
    def delete(self, id: int) -> None: pass

    @abstractmethod
    def update(self, id: int, name: str) -> UserEntity: pass
