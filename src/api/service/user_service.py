from typing import List, Optional
from src.infraestrutura.config.jwt_security import JWTSecurity
from src.dtos.user_dto import UserCreateDTO, UserReadDTO, UserUpdateDTO
from src.entity.user_entity import UserEntity
from src.interfaces.application.interface_user_application import IUserApplication
from src.interfaces.service.interface_service_user import IServiceUser


class UserService(IServiceUser):

    def __init__(self, application: IUserApplication) -> None:
        self.application = application
        self.__jwt_security = JWTSecurity()

    def list_all(self) -> List[UserReadDTO]:
        users = self.application.list_all()
        return [self.__convert_entity_to_dto(e) for e in users]

    def get_by_id(self, id: int) -> UserReadDTO:
        entity = self.application.get_by_id(id)

        return self.__convert_entity_to_dto(entity)

    def insert_user(self, dto: UserCreateDTO) -> UserReadDTO:
        entity = UserEntity(
            name=dto.name,
            username=dto.username,
            email=dto.email,
            password=self.__jwt_security.hash_password(dto.password),
        )

        created = self.application.insert_user(entity)

        if created is None:
            return None

        return self.__convert_entity_to_dto(created)

    def delete_user(self, id: int) -> None:
        self.application.delete_user(id)

    def update_user(self, id: int, dto: UserUpdateDTO) -> UserReadDTO:
        updated = self.application.update_user(
            id=id,
            name=dto.name,
            username=dto.username,
            email=dto.email
        )

        if updated is None:
            return None

        return self.__convert_entity_to_dto(updated)

    def __convert_entity_to_dto(self, entity: UserEntity) -> UserReadDTO:
        return UserReadDTO(
            id=entity.id,
            name=entity.name,
            username=entity.username,
            email=entity.email,
            active=entity.active,
            created_at=entity.created_at
        )
