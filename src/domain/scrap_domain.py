from datetime import datetime, timedelta
from typing import Optional
from src.data.database.unity_of_work import UnityOfWork
from src.entity.scrap_entity import EScrapStatus, ScrapEntity
from src.exceptions.exceptions import ServiceError
from src.infraestrutura.config.env_config import ENV_CONFIG
from src.interfaces.domain.interface_scrap_domain import IScrapDomain
from src.interfaces.infrastructure.interface_scrap_repository import IScrapRepository


class ScrapDomain(IScrapDomain):

    def __init__(self, repository: IScrapRepository):
        self.__repository = repository

    def attach_uow(self, uow: UnityOfWork):
        self.__repository.attach_uow(uow)

    def can_start_scraping(self) -> None:
        last = self.__repository.get_last_execution()

        if not last:
            return

        if last.status == EScrapStatus.RUNNING:
            raise ServiceError("Scraping já está em execução.")

        if last.finished_at:
            delta = datetime.utcnow() - last.finished_at
            if delta < timedelta(minutes=ENV_CONFIG["SCRAPING_COOLDOWN_MINUTES"]):
                raise ServiceError(
                    f"Scraping já foi executado recentemente "
                    f"({int(delta.total_seconds() / 60)} min atrás)."
                )

    def create_execution(self) -> ScrapEntity:
        try:
            return self.__repository.create_execution()
        except Exception as e:
            raise ServiceError("Erro ao iniciar execução do scraping.") from e

    def save_category_with_books(self, category: dict, books: list[dict]) -> None:
        try:
            self.__repository.save_category_with_books(category, books)
        except Exception as e:
            raise ServiceError("Erro ao salvar livros e categorias.") from e
        
    def mark_finished(self, entity: ScrapEntity) -> None:
        try:
            self.__repository.mark_finished(entity)
        except Exception as e:
            raise ServiceError("Erro ao finalizar scraping.") from e

    def get_last_execution(self) -> Optional[ScrapEntity]:
        try:
            return self.__repository.get_last_execution()
        except Exception as e:
            raise ServiceError("Erro ao buscar status do scraping") from e

    def mark_error(self, entity: ScrapEntity, error: Exception) -> None:
        try:
            self.__repository.mark_error(entity, error)
        except Exception as e:
            raise ServiceError("Erro ao marcar scraping como erro.") from e