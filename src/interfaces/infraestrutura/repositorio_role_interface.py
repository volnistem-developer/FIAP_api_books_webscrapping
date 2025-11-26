from abc import ABC, abstractmethod

from src.entidades.role_entity import RoleEntity


class IRepositorioRole(ABC):
    @abstractmethod
    def list(self) -> list[RoleEntity]:
        pass
