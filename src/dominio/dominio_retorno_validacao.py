from src.interfaces.dominio.retorno_validacao_interface import IRetornoValidacao


class DominioRetornoValidacao(IRetornoValidacao):
    def __init__(self) -> None:
        self.__excecoes: list[Exception] = []

    def add_exception(self, ex: Exception) -> None:
        self.__excecoes.append(ex)

    def has_exceptions(self) -> bool:
        return len(self.__excecoes) > 0

    def get_exceptions(self) -> list[Exception]:
        return self.__excecoes
