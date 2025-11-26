from src.aplicacao.aplicacao_role import AplicacaoRole
from src.interfaces.aplicacao.aplicacao_role_interface import IAplicacaoRole


class ServiceRole:
    def __init__(self) -> None:
        self.aplicacao = AplicacaoRole()

    def list_all(self):
        return self.aplicacao.list_all()
