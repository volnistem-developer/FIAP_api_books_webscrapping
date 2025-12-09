from src.dominio.dominio_retorno_validacao import DominioRetornoValidacao
from src.dominio.dominio_user import DominioUser
from src.entidades.user_entity import UserEntity
from src.infraestrutura.repositorio_user import RepositorioUser


class AplicacaoUser():
    def __init__(self) -> None:
        self.__retorno = DominioRetornoValidacao()
        self.dominio = DominioUser(retorno_validacao=self.__retorno)

    def list_all(self) -> list[UserEntity]:
        return self.dominio.list()
    
    def get_by_id(self, id: int) -> UserEntity:
        return self.dominio.get(id)
    
    def get_by_username(self, username: str) -> UserEntity:
        return self.dominio.get_by_username(username)

    def insert_user(self, entidade: UserEntity) -> UserEntity | None:
        return self.dominio.insert(entidade)
    
    def delete_user(self, id:int) -> None:
        self.dominio.delete(id)

    def update_user(self, id:int, name:str) -> UserEntity:
        return self.dominio.update(id, name)

    def get_validacao(self):
        return self.__retorno
