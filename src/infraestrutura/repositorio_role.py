from src.dados.database.db import Database
from src.entidades.role_entity import RoleEntity
from src.interfaces.infraestrutura.repositorio_role_interface import IRepositorioRole


class RepositorioRole(IRepositorioRole):

    def list(self):
        with Database() as db:
            return db.query(RoleEntity).filter(RoleEntity.active).all()
    
    def get(self, id: int) -> RoleEntity:
        with Database() as db:
            entity = db.query(RoleEntity).filter(RoleEntity.id == id).one()

            return entity

    def insert(self, entity: RoleEntity) -> RoleEntity:
        with Database() as db:
            db.add(entity)
            db.commit()
            db.expunge(entity)

            return entity
    
    def delete(self, id: int) -> None:
        with Database() as db:
            entity = db.query(RoleEntity).filter(RoleEntity.id == id).one()

            entity.active = False
            
            db.commit()
    
    def update(self, id, name) -> RoleEntity:
        with Database() as db:
            entity = db.query(RoleEntity).filter(RoleEntity.id == id).one()

            entity.name = name

            db.commit()
            db.expunge(entity)

            return entity