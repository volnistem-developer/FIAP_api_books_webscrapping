from abc import ABC, abstractmethod
from typing import List

from src.entity.category_entity import CategoryEntity


class ICategoryApplication(ABC):

    @abstractmethod
    def list_all_categories(self) -> List[CategoryEntity]:
        """
        Retorna todas as categorias cadastradas.
        """
        pass