from abc import ABC, abstractmethod
from typing import List, Tuple, Optional

from src.entity.book_entity import BookEntity
from src.entity.category_entity import CategoryEntity


from abc import ABC, abstractmethod
from typing import List, Tuple, Optional

from decimal import Decimal



class IBookRepository(ABC):

    @abstractmethod
    def get_or_create(self, book: dict) -> BookEntity:
        """
        Busca um livro pelo slug ou cria um novo registro.
        """
        pass

    @abstractmethod
    def link_category(self, book: BookEntity, category: CategoryEntity) -> None:
        """
        Vincula uma categoria a um livro, se ainda não estiver vinculada.
        """
        pass

    @abstractmethod
    def get_all_books(self, page: int, page_size: int) -> Tuple[List[BookEntity], int]:
        """
        Retorna livros paginados e o total geral.
        """
        pass

    @abstractmethod
    def get_all_books_most_rated(self, page: int, page_size: int) -> Tuple[List[BookEntity], int]:
        """
        Retorna livros com rating máximo (ex: 5 estrelas), paginados.
        """
        pass

    @abstractmethod
    def get_book(self, id: int) -> Optional[BookEntity]:
        """
        Retorna um livro pelo ID.
        """
        pass

    @abstractmethod
    def get_by_price_range(self, price_min: float, price_max: float) -> List[BookEntity]:
        """
        Retorna livros dentro de uma faixa de preço.
        """
        pass

    @abstractmethod
    def get_books_from_title_or_category(
        self,
        title: Optional[str] = None,
        category: Optional[str] = None
    ) -> List[BookEntity]:
        """
        Busca livros por título e/ou categoria.
        """
        pass

    # --------------------
    # Métodos de estatística
    # --------------------

    @abstractmethod
    def count_all(self) -> int:
        """
        Retorna o total de livros cadastrados.
        """
        pass

    @abstractmethod
    def count_available(self) -> int:
        """
        Retorna o total de livros disponíveis.
        """
        pass

    @abstractmethod
    def get_average_rating(self) -> float:
        """
        Retorna a média de avaliação dos livros.
        """
        pass

    @abstractmethod
    def get_average_price_brl(self) -> float:
        """
        Retorna o preço médio dos livros em reais.
        """
        pass

    @abstractmethod
    def get_stats_by_category(self):
        """
        Retorna estatísticas agregadas por categoria:
        - total de livros
        - disponíveis
        - média de rating
        - média de preço bruto
        """
        pass

    @abstractmethod
    def get_availability_stats(self) -> dict:
        """
        Retorna estatísticas gerais de disponibilidade:
        - total
        - disponíveis
        - indisponíveis
        """
        pass

