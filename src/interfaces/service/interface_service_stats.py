from abc import ABC, abstractmethod
from typing import Any, Dict, List

from src.dtos.stats_dto import AvailabilityStatsDTO, CategoryStatsDTO, OverviewDTO


class IStatsService(ABC):

    @abstractmethod
    def get_overview(self) -> OverviewDTO:
        """
        Retorna estatísticas gerais da aplicação:
        - total de livros
        - disponíveis
        - indisponíveis
        - média de rating
        - preço médio em BRL
        - data da última execução do scrap
        """
        pass

    @abstractmethod
    def get_categories_stats(self) -> list[CategoryStatsDTO]:
        """
        Retorna estatísticas agregadas por categoria:
        - nome da categoria
        - total de livros
        - disponíveis
        - média de rating
        - preço médio em BRL
        """
        pass

    @abstractmethod
    def get_availability_stats(self) -> AvailabilityStatsDTO:
        """
        Retorna estatísticas de disponibilidade:
        - total de livros
        - disponíveis
        - indisponíveis
        - taxa de disponibilidade (%)
        """
        pass