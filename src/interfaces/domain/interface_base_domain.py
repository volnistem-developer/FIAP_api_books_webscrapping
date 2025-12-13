from abc import ABC, abstractmethod

from src.domain.exceptions import AppException


class IBaseDomain(ABC):

    @property
    @abstractmethod
    def validation(self) -> list[AppException]: pass

    @abstractmethod
    def add_validation(self, ex: AppException) -> None: pass
