from abc import ABC, abstractmethod


class IRetornoValidacao(ABC):
    @abstractmethod
    def add_exception(self, ex: Exception) -> None:
        pass

    @abstractmethod
    def has_exceptions(self) -> bool:
        pass

    @abstractmethod
    def get_exceptions(self) -> list[Exception]:
        pass
