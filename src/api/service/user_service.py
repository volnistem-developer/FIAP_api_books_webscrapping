from passlib.context import CryptContext

from src.aplicacao.aplicacao_user import AplicacaoUser
from src.dtos.user_dto import UserCreateDTO, UserReadDTO
from src.entidades.user_entity import UserEntity


class ServiceUser:
    '''Transformar Entidade -> para DTO para retornar para a controller'''

    def __init__(self) -> None:
        self.aplicacao = AplicacaoUser()

    def list_all(self):
        retorno = self.aplicacao.list_all()

        users_list: list[UserReadDTO] = [self.convert_entity_to_dto(e) for e in retorno]

        return users_list
    
    def get_by_id(self, id:int):
        retorno = self.aplicacao.get_by_id(id)

        return retorno
    
    
    def insert_user(self, dto: UserCreateDTO):

        bcrypt_context = CryptContext(schemes=['argon2'])

        entidade = UserEntity(
            name=dto.name,
            username=dto.username,
            email=dto.email,
            password=bcrypt_context.hash(dto.password),
        )

        retorno = self.aplicacao.insert_user(entidade)

        return retorno
    
    def delete_user(self, id:int):
        self.aplicacao.delete_user(id)

    def update_user(self, id, dto: UserCreateDTO):
        retorno = self.aplicacao.update_user(id, dto.name)

        return retorno
    
    def convert_entity_to_dto(self,entity: UserEntity) -> UserReadDTO:
        return UserReadDTO(
            id=entity.id,
            name=entity.name,
            username=entity.username,
            email=entity.email,
            active=entity.active,
            created_at=entity.created_at
        )
    
    def has_exceptions(self):
        return self.aplicacao.get_validacao().has_exceptions()

    def get_exceptions(self):
        return self.aplicacao.get_validacao().get_exceptions()