from abc import ABC, abstractmethod
from typing import Any, Dict


class IScrapApplication(ABC):

    @abstractmethod
    def start_scraping(self) -> None:
        """
        Inicia o processo de scraping em background.
        Lança exceção se o scraping já estiver em execução
        ou se estiver em período de cooldown.
        """
        pass

    @abstractmethod
    def get_status(self) -> Dict[str, Any]:
        """
        Retorna o status da última execução de scraping.

        Exemplo de retorno:
        {
            "status": "RUNNING" | "FINISHED" | "ERROR" | "never_executed",
            "started_at": datetime | None,
            "finished_at": datetime | None,
            "error": str | None
        }
        """
        pass