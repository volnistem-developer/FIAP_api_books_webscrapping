from src.data.database.db import Database
from src.entity.user_entity import UserEntity
from src.interfaces.infrastructure.interface_user_repository import IUserRepository

class UserRepository(IUserRepository):

    def __init__(self, db_connection: Database):
        self.__db_connection = db_connection

    def list(self):
        with self.__db_connection as db:
            return db.query(UserEntity).filter(UserEntity.active).all()

    def get(self, id: int) -> UserEntity:
        with self.__db_connection as db:
            entity = db.query(UserEntity).filter(UserEntity.id == id).one()

            return entity
    
    def get_by_username(self, username: str) -> UserEntity:
        with self.__db_connection as db:
            entity = db.query(UserEntity).filter(UserEntity.username == username).one()

            return entity
    
    def insert(self, entity: UserEntity) -> UserEntity:
        with self.__db_connection as db:
            db.add(entity)
            db.commit()
            db.expunge(entity)

            return entity
    
    def delete(self, id: int) -> None:
        with self.__db_connection as db:
            entity = db.query(UserEntity).filter(UserEntity.id == id and UserEntity.active).one()

            entity.active = False
            
            db.commit()
    
    def update(self, id, name, username, email) -> UserEntity:
        with self.__db_connection as db:
            entity = db.query(UserEntity).filter(UserEntity.id == id and UserEntity.active).one()

            entity.name = name
            entity.username = username
            entity.username = email

            db.commit()
            db.expunge(entity)

            return entity
    