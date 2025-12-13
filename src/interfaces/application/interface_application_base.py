from abc import ABC, abstractmethod

from src.domain.exceptions import AppException


class IApplicationBase(ABC):
    
    @property
    @abstractmethod
    def validation(self) -> list[AppException]: pass