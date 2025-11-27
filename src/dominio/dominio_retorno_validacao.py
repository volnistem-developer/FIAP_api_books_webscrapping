from src.dominio.exceptions import AppException
from src.interfaces.dominio.retorno_validacao_interface import IRetornoValidacao


class DominioRetornoValidacao(IRetornoValidacao):
    def __init__(self) -> None:
        self.__excecoes: list[AppException] = []

    def add_exception(self, ex: Exception) -> None:
        self.__excecoes.append(ex)

    def has_exceptions(self) -> bool:
        return len(self.__excecoes) > 0

    def get_exceptions(self) -> list[AppException]:
        return self.__excecoes
