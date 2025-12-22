from abc import ABC, abstractmethod
from typing import Dict, List, Optional

from src.dtos.book_dto import BookReadDTO


class IBookService(ABC):

    @abstractmethod
    def get_all_books(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retorna todos os livros paginados.
        """
        pass

    @abstractmethod
    def get_all_books_most_rated(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retorna os livros mais bem avaliados (rating 5),
        paginados.
        """
        pass

    @abstractmethod
    def get_book(self, id: int) -> BookReadDTO:
        """
        Retorna um livro pelo ID.
        """
        pass

    @abstractmethod
    def get_books_from_title_or_category(self, title: Optional[str], category: Optional[str]) -> List[BookReadDTO]:
        """
        Busca livros pelo título e/ou categoria.
        """
        pass

    @abstractmethod
    def get_by_price_range(self, price_min: float, price_max: float) -> List[BookReadDTO]:
        """
        Retorna livros dentro de um intervalo de preço.
        """
        pass