from abc import ABC, abstractmethod

from src.data.database.unity_of_work import UnityOfWork


class IStatsDomain(ABC):

    @abstractmethod
    def attach_uow(self, uow: UnityOfWork) -> None:
        pass

    @abstractmethod
    def get_overview(self) -> dict:
        """
        Retorna estatísticas gerais da aplicação:
        - total de livros
        - disponibilidade
        - médias
        - última execução de scraping
        """
        pass

    @abstractmethod
    def get_categories_stats(self) -> list[dict]:
        """
        Retorna estatísticas agregadas por categoria:
        - total de livros
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