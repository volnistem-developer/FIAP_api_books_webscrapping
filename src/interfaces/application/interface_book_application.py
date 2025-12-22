from abc import ABC, abstractmethod
from typing import Optional, List

from src.entity.book_entity import BookEntity


class IBookApplication(ABC):

    @abstractmethod
    def list_all_books(
        self,
        page: int,
        page_size: int
    ) -> List[BookEntity]:
        """
        Lista todos os livros com paginação.
        """
        pass

    @abstractmethod
    def get_all_books_most_rated(
        self,
        page: int,
        page_size: int
    ) -> List[BookEntity]:
        """
        Lista livros mais bem avaliados (ex: rating = 5), com paginação.
        """
        pass

    @abstractmethod
    def get_book(
        self,
        id: int
    ) -> BookEntity:
        """
        Retorna um livro pelo ID.
        Lança exceção se não existir.
        """
        pass

    @abstractmethod
    def get_by_price_range(
        self,
        price_min: float,
        price_max: float
    ) -> List[BookEntity]:
        """
        Retorna livros dentro de um intervalo de preço.
        Valores recebidos em reais (float),
        persistência em centavos é responsabilidade interna.
        """
        pass

    @abstractmethod
    def get_books_from_title_or_category(
        self,
        title: Optional[str],
        category: Optional[str]
    ) -> List[BookEntity]:
        """
        Busca livros por título e/ou categoria.
        Ambos os parâmetros são opcionais.
        """
        pass