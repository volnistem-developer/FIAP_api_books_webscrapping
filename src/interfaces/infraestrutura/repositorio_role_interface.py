from abc import ABC, abstractmethod

from src.entidades.role_entity import RoleEntity


class IRepositorioRole(ABC):
    @abstractmethod
    def list(self) -> list[RoleEntity]: pass

    @abstractmethod
    def get(self, id: int) -> RoleEntity: pass

    @abstractmethod
    def insert(self, entity: RoleEntity) -> RoleEntity: pass

    @abstractmethod
    def delete(self, id: int) -> None: pass

    @abstractmethod
    def update(self, id: int, name: str) -> RoleEntity: pass
