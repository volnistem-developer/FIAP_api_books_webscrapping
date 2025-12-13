from abc import abstractmethod

from src.dtos.user_dto import UserCreateDTO, UserReadDTO
from src.interfaces.service.interface_service_base import IServiceBase


class IServiceUser(IServiceBase):

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
