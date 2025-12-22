from abc import ABC, abstractmethod
from typing import Optional

from src.data.database.unity_of_work import UnityOfWork
from src.entity.scrap_entity import ScrapEntity


class IScrapRepository(ABC):

    @abstractmethod
    def attach_uow(self, uow: UnityOfWork) -> None:
        """
        Associa a Unit of Work ao repositório e
        inicializa os repositórios dependentes.
        """
        pass

    @abstractmethod
    def get_last_execution(self) -> Optional[ScrapEntity]:
        """
        Retorna a última execução de scraping
        ou None se nunca foi executado.
        """
        pass

    @abstractmethod
    def create_execution(self) -> ScrapEntity:
        """
        Cria um novo registro de execução de scraping
        com status RUNNING.
        """
        pass

    @abstractmethod
    def mark_finished(self, entity: ScrapEntity) -> None:
        """
        Marca uma execução de scraping como finalizada.
        """
        pass

    @abstractmethod
    def mark_error(self, entity: ScrapEntity, error: Exception) -> None:
        """
        Marca uma execução de scraping como erro.
        """
        pass

    @abstractmethod
    def save_category_with_books(self, category: dict, books: list[dict]) -> None:
        """
        Persiste uma categoria e seus livros associados.
        Utiliza BookRepository e CategoryRepository.
        """
        pass