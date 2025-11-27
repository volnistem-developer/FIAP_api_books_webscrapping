from abc import ABC, abstractmethod

from src.dominio.exceptions import AppException


class IRetornoValidacao(ABC):
    @abstractmethod
    def add_exception(self, ex: AppException) -> None:
        pass

    @abstractmethod
    def has_exceptions(self) -> bool:
        pass

    @abstractmethod
    def get_exceptions(self) -> list[AppException]:
        pass
