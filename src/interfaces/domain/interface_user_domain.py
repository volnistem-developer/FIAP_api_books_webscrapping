from abc import ABC, abstractmethod
from typing import List

from src.data.database.unity_of_work import UnityOfWork
from src.entity.user_entity import UserEntity

class IUserDomain(ABC):

    @abstractmethod
    def attach_uow(self, uow: UnityOfWork) -> None:
        """
        Associa a Unit of Work ao domínio.
        """
        pass

    @abstractmethod
    def list(self) -> List[UserEntity]:
        """
        Retorna todos os usuários ativos.
        """
        pass

    @abstractmethod
    def get(self, id: int) -> UserEntity:
        """
        Retorna um usuário pelo ID.
        Lança exceção se não existir.
        """
        pass

    @abstractmethod
    def get_by_username(self, username: str) -> UserEntity:
        """
        Retorna um usuário pelo username.
        Lança exceção se não existir.
        """
        pass

    @abstractmethod
    def insert(self, entidade: UserEntity) -> UserEntity:
        """
        Cria um novo usuário.
        """
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        """
        Desativa (soft delete) um usuário.
        """
        pass

    @abstractmethod
    def update(self,id: int,name: str,username: str,email: str) -> UserEntity:
        """
        Atualiza os dados do usuário.
        """
        pass
