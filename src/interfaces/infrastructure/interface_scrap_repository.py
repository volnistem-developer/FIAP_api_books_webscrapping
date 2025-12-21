from abc import ABC, abstractmethod

from src.entity.scrap_entity import ScrapEntity


class IScrapRepository(ABC):

    @abstractmethod
    def save_category_with_books(self, category: dict, books: list[dict]) -> None: pass
    
    @abstractmethod
    def get_last_execution(self) -> (ScrapEntity | None): pass

    @abstractmethod
    def create_execution(self) -> ScrapEntity: pass

    @abstractmethod
    def mark_finished(self, entity: ScrapEntity) -> None: pass

    @abstractmethod
    def mark_error(self, entity: ScrapEntity, error: Exception) -> None: pass