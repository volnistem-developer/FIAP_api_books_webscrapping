
from abc import ABC, abstractmethod
from typing import List

from src.dtos.category_dto import CategoryReadDTO


class IServiceCategory(ABC):

    @abstractmethod
    def list_all_categories(self) -> List[CategoryReadDTO]:
        """
        Retorna todas as categorias disponíveis.
        """
        pass