from abc import ABC, abstractmethod
from typing import List

from src.data.database.unity_of_work import UnityOfWork
from src.entity.category_entity import CategoryEntity



class ICategoryDomain(ABC):

    @abstractmethod
    def attach_uow(self, uow: UnityOfWork) -> None:
        """
        Associa a Unit of Work ao domínio.
        """
        pass

    @abstractmethod
    def list_all_categories(self) -> List[CategoryEntity]:
        """
        Retorna todas as categorias cadastradas.
        """
        pass