from abc import ABC, abstractmethod

from src.dtos.user_dto import UserCreateDTO, UserReadDTO


class IServiceUser(ABC):

    @abstractmethod
    def list_all(self) -> list[UserReadDTO]: pass

    @abstractmethod
    def get_by_id(self, id:int) -> UserReadDTO | None: pass

    @abstractmethod
    def insert_user(self, dto: UserCreateDTO) -> UserReadDTO | None: pass

    @abstractmethod
    def delete_user(self, id:int) -> None: pass

    @abstractmethod
    def update_user(self, id, dto: UserCreateDTO) -> UserReadDTO | None: pass
