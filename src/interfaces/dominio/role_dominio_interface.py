from abc import ABC, abstractmethod

from src.entidades.role_entity import RoleEntity


class IDominioRole(ABC):
    @abstractmethod
    def list_all(self) -> RoleEntity:
        pass
