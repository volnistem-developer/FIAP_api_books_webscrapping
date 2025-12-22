from abc import ABC, abstractmethod
from typing import List, Optional

from src.data.database.unity_of_work import UnityOfWork
from src.entity.book_entity import BookEntity


class IBookDomain(ABC):

    @abstractmethod
    def attach_uow(self, uow: UnityOfWork) -> None:
        """
        Associa a Unit of Work ao domínio.
        """
        pass

    @abstractmethod
    def list_all_books(self, page: int, page_size: int) -> List[BookEntity]:
        """
        Lista todos os livros com paginação.
        """
        pass
        
    @abstractmethod
    def get_all_books_most_rated(self, page: int, page_size: int) -> List[BookEntity]:
        """
        Lista os livros mais bem avaliados (ex: rating = 5),
        com paginação.
        """
        pass
        
    @abstractmethod
    def get_book(self, id: int) -> BookEntity:
        """
        Retorna um livro pelo ID.
        Lança exceção se não existir.
        """
        pass
        
    @abstractmethod
    def get_by_price_range(self, price_min: float, price_max: float) -> List[BookEntity]:
        """
        Retorna livros dentro de um intervalo de preço.
        Valores recebidos em reais (float).
        """
        pass
        
    @abstractmethod
    def get_books_from_title_or_category(self, title: Optional[str], category: Optional[str]) -> List[BookEntity]:
        """
        Busca livros por título e/ou categoria.
        """
        pass