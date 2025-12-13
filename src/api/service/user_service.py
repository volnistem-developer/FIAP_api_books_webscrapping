from src.infraestrutura.service.jwt_security import JWTSecurity
from src.dtos.user_dto import UserCreateDTO, UserReadDTO
from src.entity.user_entity import UserEntity
from src.interfaces.application.interface_application_user import IUserApplication
from src.interfaces.service.interface_service_user import IServiceUser


class UserService(IServiceUser):

    def __init__(self, application: IUserApplication) -> None:
        self.application = application
        self.__jwt_security = JWTSecurity()
    
    @property
    def validation(self):
        return self.application.validation

    def list_all(self) -> list[UserReadDTO]:
        response = self.application.list_all()

        users_list: list[UserReadDTO] = [self.__convert_entity_to_dto(e) for e in response]

        return users_list
    
    def get_by_id(self, id:int) -> UserReadDTO | None:

        response = self.application.get_by_id(id)

        if response is None:
            return None

        return self.__convert_entity_to_dto(response)
    
    def insert_user(self, dto: UserCreateDTO) -> UserReadDTO | None:
        
        entidade = UserEntity(
            name=dto.name,
            username=dto.username,
            email=dto.email,
            password=self.__jwt_security.hash_password(dto.password),
        )

        response = self.application.insert_user(entidade)

        if response is None:
            return None
        else:
            return self.__convert_entity_to_dto(response)
    
    def delete_user(self, id:int) -> None:
        self.application.delete_user(id)

    def update_user(self, id, dto: UserCreateDTO) -> UserReadDTO | None:
        response = self.application.update_user(id, dto.name)

        if response is None:
            return None
        else:
            return self.__convert_entity_to_dto(response)
    
    def __convert_entity_to_dto(self,entity: UserEntity) -> UserReadDTO:
        return UserReadDTO(
            id=entity.id,
            name=entity.name,
            username=entity.username,
            email=entity.email,
            active=entity.active,
            created_at=entity.created_at
        )