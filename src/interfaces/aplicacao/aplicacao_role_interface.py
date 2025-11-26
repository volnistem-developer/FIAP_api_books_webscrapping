from abc import ABC, abstractmethod

from src.entidades.role_entity import RoleEntity


class IAplicacaoRole(ABC):
    @abstractmethod
    def list_all(self) -> list[RoleEntity]:
        pass
