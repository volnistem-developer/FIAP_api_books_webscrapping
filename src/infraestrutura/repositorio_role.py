from src.dados.database.db import Database
from src.entidades.role_entity import RoleEntity
from src.interfaces.infraestrutura.repositorio_role_interface import IRepositorioRole


class RepositorioRole(IRepositorioRole):
    def list(self):
        with Database() as db:
            return db.query(RoleEntity).all()
