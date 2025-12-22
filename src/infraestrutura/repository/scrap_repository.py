from datetime import datetime
from typing import Optional
from src.data.database.unity_of_work import UnityOfWork
from src.entity.scrap_entity import EScrapStatus, ScrapEntity
from src.infraestrutura.repository.book_repository import BookRepository
from src.infraestrutura.repository.category_repository import CategoryRepository
from src.interfaces.infrastructure.interface_scrap_repository import IScrapRepository


class ScrapRepository(IScrapRepository):

    def __init__(self):
        self.uow: UnityOfWork | None = None
        self.book_repository: BookRepository | None = None
        self.category_repository: CategoryRepository | None = None

    def attach_uow(self, uow: UnityOfWork) -> None:
        self.uow = uow
        self.book_repository = BookRepository(uow)
        self.category_repository = CategoryRepository(uow)


    def get_last_execution(self) -> Optional[ScrapEntity]:
        return (
            self.uow.session
            .query(ScrapEntity)
            .order_by(ScrapEntity.started_at.desc())
            .first()
        )
    
    def create_execution(self) -> ScrapEntity:
        entity = ScrapEntity(
            status=EScrapStatus.RUNNING,
            started_at=datetime.utcnow()
        )
        self.uow.session.add(entity)
        self.uow.session.flush()  # garante ID
        return entity
    
    def mark_finished(self, entity: ScrapEntity) -> None:
        entity.status = EScrapStatus.FINISHED
        entity.finished_at = datetime.utcnow()

    def mark_error(self, entity: ScrapEntity, error: Exception) -> None:
        entity.status = EScrapStatus.ERROR
        entity.finished_at = datetime.utcnow()
        entity.error_message = str(error)

    def save_category_with_books(self, category: dict, books: list[dict]) -> None:
        category_entity = self.category_repository.get_or_create(category["name"])

        for book in books:
            book_entity = self.book_repository.get_or_create(book)
            self.book_repository.link_category(book_entity, category_entity)