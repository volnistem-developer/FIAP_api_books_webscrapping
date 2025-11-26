from src.dominio.dominio_retorno_validacao import DominioRetornoValidacao
from src.dominio.dominio_role import DominioRole
from src.entidades.role_entity import RoleEntity
from src.infraestrutura.repositorio_role import RepositorioRole
from src.interfaces.aplicacao.aplicacao_role_interface import IAplicacaoRole


class AplicacaoRole(IAplicacaoRole):
    def __init__(self) -> None:
        retorno = DominioRetornoValidacao()
        repo = RepositorioRole()

        self.dominio = DominioRole(repositorio=repo, retorno_validacao=retorno)

    def list_all(self) -> list[RoleEntity]:
        return self.dominio.list()
