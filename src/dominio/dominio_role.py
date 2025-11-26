from src.dominio.dominio_base import DominioBase
from src.entidades.role_entity import RoleEntity
from src.infraestrutura.repositorio_role import RepositorioRole
from src.interfaces.dominio.retorno_validacao_interface import IRetornoValidacao
from src.interfaces.infraestrutura.repositorio_role_interface import IRepositorioRole


class DominioRole(DominioBase):
    def __init__(
        self, repositorio: IRepositorioRole, retorno_validacao: IRetornoValidacao
    ) -> None:
        super().__init__(retorno_validacao)
        self.__repositorio = repositorio

    def list(self) -> list[RoleEntity]:
        retorno: list[RoleEntity] = []

        try:
            retorno = self.__repositorio.list()

        except Exception as ex:
            self.retorno_validacao.add_exception(ex)

        return retorno
