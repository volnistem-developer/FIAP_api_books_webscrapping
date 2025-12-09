from src.dados.database.db import Database
from src.entidades.user_entity import UserEntity
from src.interfaces.infraestrutura.repositorio_user_interface import IRepositorioUser

class RepositorioUser(IRepositorioUser):

    def list(self):
        with Database() as db:
            return db.query(UserEntity).filter(UserEntity.active).all()

    def get(self, id: int) -> UserEntity:
        with Database() as db:
            entity = db.query(UserEntity).filter(UserEntity.id == id).one()

            return entity
    
    def get_by_username(self, username: str) -> UserEntity:
        with Database() as db:
            entity = db.query(UserEntity).filter(UserEntity.username == username).one()

            return entity
    
    def insert(self, entity: UserEntity) -> UserEntity:
        with Database() as db:
            db.add(entity)
            db.commit()
            db.expunge(entity)

            return entity
    
    def delete(self, id: int) -> None:
        with Database() as db:
            entity = db.query(UserEntity).filter(UserEntity.id == id).one()

            entity.active = False
            
            db.commit()
    
    def update(self, id, name, username, email) -> UserEntity:
        with Database() as db:
            entity = db.query(UserEntity).filter(UserEntity.id == id and UserEntity.active).one()

            entity.name = name
            entity.username = username
            entity.username = email

            db.commit()
            db.expunge(entity)

            return entity
    