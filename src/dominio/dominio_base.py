from src.interfaces.dominio.retorno_validacao_interface import IRetornoValidacao


class DominioBase:
    def __init__(self, retorno_validacao: IRetornoValidacao) -> None:
        self.retorno_validacao = retorno_validacao

    def validation(self) -> IRetornoValidacao:
        return self.retorno_validacao
