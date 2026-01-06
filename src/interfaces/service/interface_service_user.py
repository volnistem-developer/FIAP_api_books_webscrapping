from abc import ABC, abstractmethod
from typing import List, Optional

from src.dtos.user_dto import UserCreateDTO, UserReadDTO, UserUpdateDTO


class IServiceUser(ABC):

    @abstractmethod
    def list_all(self) -> List[UserReadDTO]:
        """
        Retorna todos os usuários ativos.
        """
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> UserReadDTO:
        """
        Retorna um usuário pelo ID ou None se não existir.
        """
        pass

    @abstractmethod
    def insert_user(self, dto: UserCreateDTO) -> UserReadDTO:
        """
        Cria um novo usuário.
        """
        pass

    @abstractmethod
    def delete_user(self, id: int) -> None:
        """
        Remove (desativa) um usuário.
        """
        pass

    @abstractmethod
    def update_user(self, id: int, dto: UserUpdateDTO) -> UserReadDTO:
        """
        Atualiza os dados de um usuário.
        """
        pass
