from abc import ABC, abstractmethod
from typing import List, Tuple, Optional

from src.data.database.unity_of_work import UnityOfWork
from src.entity.book_entity import BookEntity
from src.entity.category_entity import CategoryEntity


class IBookRepository(ABC):

    @abstractmethod
    def __init__(self, uow: UnityOfWork):
        """
        Inicializa o repositório com uma Unit of Work.
        """
        pass

    @abstractmethod
    def get_or_create(self, book: dict) -> BookEntity:
        """
        Retorna um livro existente pelo slug ou cria um novo.
        Utilizado no processo de scraping.
        """
        pass

    @abstractmethod
    def link_category(self, book: BookEntity, category: CategoryEntity) -> None:
        """
        Associa uma categoria a um livro.
        """
        pass

    @abstractmethod
    def get_all_books(self, page: int, page_size: int) -> Tuple[List[BookEntity], int]:
        """
        Retorna livros paginados e o total de registros.
        """
        pass

    @abstractmethod
    def get_all_books_most_rated(self, page: int, page_size: int) -> Tuple[List[BookEntity], int]:
        """
        Retorna livros com maior avaliação (rating = 5),
        paginados e com total.
        """
        pass

    @abstractmethod
    def get_book(self, id: int) -> Optional[BookEntity]:
        """
        Retorna um livro pelo ID ou None se não existir.
        """
        pass

    @abstractmethod
    def get_by_price_range(self, price_min: float, price_max: float) -> List[BookEntity]:
        """
        Retorna livros dentro de um intervalo de preço.
        Valores recebidos em libras esterlinas como no site original.
        """
        pass

    @abstractmethod
    def get_books_from_title_or_category(self, title: Optional[str] = None, category: Optional[str] = None) -> List[BookEntity]:
        """
        Busca livros por título e/ou categoria.
        """
        pass
