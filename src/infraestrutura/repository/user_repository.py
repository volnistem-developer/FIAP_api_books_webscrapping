from src.data.database.unity_of_work import UnityOfWork
from src.entity.user_entity import UserEntity
from src.interfaces.infrastructure.interface_user_repository import IUserRepository

class UserRepository(IUserRepository):

    def __init__(self, uow: UnityOfWork):
        self.uow = uow

    def list(self) -> list[UserEntity]:
        return (
            self.uow.session
            .query(UserEntity)
            .filter(UserEntity.active == True)
            .all()
        )

    def get(self, id: int) -> UserEntity:
        return (
            self.uow.session
            .query(UserEntity)
            .filter(UserEntity.id == id)
            .one_or_none()
        )
    
    def get_by_username(self, username: str) -> UserEntity:
        return (
            self.uow.session
            .query(UserEntity)
            .filter(UserEntity.username == username)
            .one_or_none()
        )
    
    def get_by_email(self, email: str) -> UserEntity:
        return (
            self.uow.session
            .query(UserEntity)
            .filter(UserEntity.email == email)
            .one_or_none()
        )
    
    def insert(self, entity: UserEntity) -> UserEntity:
        self.uow.session.add(entity)
        return entity
    
    def delete(self, id: int) -> None:
        entity = (
            self.uow.session
            .query(UserEntity)
            .filter(UserEntity.id == id, UserEntity.active == True)
            .one_or_none()
        )

        entity.active = False
    
    def update(self, id: int, name: str, username: str, email: str) -> UserEntity:
        entity = (
            self.uow.session
            .query(UserEntity)
            .filter(UserEntity.id == id, UserEntity.active == True)
            .one_or_none()
        )

        entity.name = name
        entity.username = username
        entity.email = email

        return entity
    