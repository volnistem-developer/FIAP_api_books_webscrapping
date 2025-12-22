from abc import ABC, abstractmethod
from typing import List

from src.data.database.unity_of_work import UnityOfWork
from src.entity.category_entity import CategoryEntity



class ICategoryRepository(ABC):

    @abstractmethod
    def __init__(self, uow: UnityOfWork):
        """
        Inicializa o repositório com uma Unit of Work.
        """
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> CategoryEntity:
        """
        Retorna uma categoria pelo nome.
        Lança exceção se não existir.
        """
        pass

    @abstractmethod
    def get_all(self) -> List[CategoryEntity]:
        """
        Retorna todas as categorias.
        """
        pass

    @abstractmethod
    def get_or_create(self, name: str) -> CategoryEntity:
        """
        Retorna uma categoria existente pelo nome
        ou cria uma nova se não existir.
        Utilizado no processo de scraping.
        """
        pass