from abc import ABC, abstractmethod


class IScrapApplication(ABC):

    @abstractmethod
    def start_scraping(self) -> None: pass

    @abstractmethod
    def get_status(self) -> dict: pass