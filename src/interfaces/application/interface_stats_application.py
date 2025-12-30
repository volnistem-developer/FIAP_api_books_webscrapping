from abc import ABC, abstractmethod


class IStatsApplication(ABC):

    @abstractmethod
    def get_overview(self) -> dict:
        """
        Retorna estatísticas gerais da aplicação:
        - total de livros
        - disponibilidade
        - média de rating
        - média de preço
        - última execução do scraping
        """
        pass

    @abstractmethod
    def get_categories_stats(self) -> list[dict]:
        """
        Retorna estatísticas agregadas por categoria:
        - quantidade de livros
        - livros disponíveis
        - média de rating
        - preço médio
        """
        pass

    @abstractmethod
    def get_availability_stats(self) -> dict:
        """
        Retorna estatísticas de disponibilidade dos livros
        (ex: disponíveis vs indisponíveis)
        """
        pass