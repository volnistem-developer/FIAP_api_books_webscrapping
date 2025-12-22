from abc import ABC, abstractmethod
from typing import List

from src.data.database.unity_of_work import UnityOfWork
from src.entity.user_entity import UserEntity

class IUserRepository(ABC):

    @abstractmethod
    def __init__(self, uow: UnityOfWork):
        """
        Inicializa o repositório com uma Unit of Work.
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
    def insert(self, entity: UserEntity) -> UserEntity:
        """
        Persiste um novo usuário.
        Commit é responsabilidade do UoW.
        """
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        """
        Realiza soft delete do usuário.
        """
        pass

    @abstractmethod
    def update(self, id: int, name: str, username: str, email: str) -> UserEntity:
        """
        Atualiza os dados do usuário.
        """
        pass
