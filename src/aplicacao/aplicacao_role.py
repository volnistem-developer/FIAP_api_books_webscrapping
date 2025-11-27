from src.dominio.dominio_retorno_validacao import DominioRetornoValidacao
from src.dominio.dominio_role import DominioRole
from src.entidades.role_entity import RoleEntity
from src.infraestrutura.repositorio_role import RepositorioRole
from src.interfaces.aplicacao.aplicacao_role_interface import IAplicacaoRole


class AplicacaoRole(IAplicacaoRole):
    def __init__(self) -> None:
        self.__retorno = DominioRetornoValidacao()
        self.__repo = RepositorioRole()

        self.dominio = DominioRole(
            repositorio=self.__repo, retorno_validacao=self.__retorno
        )

    def list_all(self) -> list[RoleEntity]:
        return self.dominio.list()
    
    def get_by_id(self, id: int) -> RoleEntity:
        return self.dominio.get(id)

    def insert_role(self, entidade: RoleEntity) -> RoleEntity | None:
        return self.dominio.insert(entidade)
    
    def delete_role(self, id:int) -> None:
        self.dominio.delete(id)

    def update_role(self, id:int, name:str) -> RoleEntity:
        return self.dominio.update(id, name)

    def get_validacao(self):
        return self.__retorno
