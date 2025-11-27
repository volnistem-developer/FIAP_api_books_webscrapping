from src.aplicacao.aplicacao_role import AplicacaoRole
from src.dtos.role_dto import RoleCreateDTO
from src.entidades.role_entity import RoleEntity


class ServiceRole:
    def __init__(self) -> None:
        self.aplicacao = AplicacaoRole()

    def list_all(self):
        retorno = self.aplicacao.list_all()

        return retorno
    
    def get_by_id(self, id:int):
        retorno = self.aplicacao.get_by_id(id)

        return retorno

    def insert_role(self, dto: RoleCreateDTO):
        entidade = RoleEntity(name=dto.name)

        retorno = self.aplicacao.insert_role(entidade)

        return retorno
    
    def delete_role(self, id:int):
        self.aplicacao.delete_role(id)

    def update_role(self, id, dto: RoleCreateDTO):
        retorno = self.aplicacao.update_role(id, dto.name)

        return retorno
    

    def has_exceptions(self):
        return self.aplicacao.get_validacao().has_exceptions()

    def get_exceptions(self):
        return self.aplicacao.get_validacao().get_exceptions()
