from abc import ABC, abstractmethod
from typing import Dict


class IServiceScrap(ABC):

    @abstractmethod
    def start_scraping(self) -> None:
        """
        Dispara o processo de scraping em background.
        """
        pass

    @abstractmethod
    def get_status(self) -> Dict:
        """
        Retorna o status da última execução do scraping.
        """
        pass