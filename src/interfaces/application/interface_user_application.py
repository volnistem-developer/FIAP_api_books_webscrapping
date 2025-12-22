from abc import ABC, abstractmethod
from typing import List

from src.entity.user_entity import UserEntity


class IUserApplication(ABC):

    @abstractmethod
    def list_all(self) -> List[UserEntity]:
        """
        Retorna todos os usuários ativos.
        """
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> UserEntity:
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
    def insert_user(self, entidade: UserEntity) -> UserEntity:
        """
        Cria um novo usuário.
        """
        pass

    @abstractmethod
    def delete_user(self, id: int) -> None:
        """
        Desativa (soft delete) um usuário.
        """
        pass

    @abstractmethod
    def update_user(self, id: int, name: str, username: str, email: str) -> UserEntity:
        """
        Atualiza dados básicos do usuário.
        """
        pass