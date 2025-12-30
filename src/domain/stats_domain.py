from src.data.database.unity_of_work import UnityOfWork
from src.exceptions.exceptions import ServiceError
from src.interfaces.domain.interface_stats_domain import IStatsDomain
from src.interfaces.infrastructure.interface_book_repository import IBookRepository
from src.interfaces.infrastructure.interface_scrap_repository import IScrapRepository


class StatsDomain(IStatsDomain):

    def __init__(self, book_repository: IBookRepository, scrap_repository: IScrapRepository):
        self.__book_repository = book_repository
        self.__scrap_repository = scrap_repository

    def attach_uow(self, uow: UnityOfWork):
        self.__book_repository.uow = uow
        self.__scrap_repository.attach_uow(uow)

    def get_overview(self) -> dict:
        try:
            total_books = self.__book_repository.count_all()
            available_books = self.__book_repository.count_available()

            average_rating = self.__book_repository.get_average_rating()
            average_price_brl = self.__book_repository.get_average_price_brl()

            last_scrap = self.__scrap_repository.get_last_execution()

            return {
                "total_books": total_books,
                "available_books": available_books,
                "unavailable_books": total_books - available_books,
                "average_rating": average_rating or 0,
                "average_price_brl": average_price_brl or 0,
                "last_scrap_execution": (
                    last_scrap.started_at if last_scrap else None
                )
            }

        except Exception as e:
            raise ServiceError(
                "Erro ao buscar estatísticas gerais da aplicação"
            ) from e
    
    def get_categories_stats(self) -> list[dict]:
        try:
            rows = self.__book_repository.get_stats_by_category()

            result: list[dict] = []

            for row in rows:
                avg_price_brl = (
                    (row.average_raw_price_in_cents / 100) * 7.41
                    if row.average_raw_price_in_cents
                    else 0
                )

                result.append({
                    "category": row.category_name,
                    "total_books": row.total_books,
                    "available_books": row.available_books or 0,
                    "average_rating": row.average_rating or 0,
                    "average_price_brl": avg_price_brl
                })

            return result

        except Exception as e:
            raise ServiceError(
                "Erro ao buscar estatísticas por categoria"
            ) from e
    
    def get_availability_stats(self) -> dict:
        try:
            return self.__book_repository.get_availability_stats()
        except Exception as e:
            raise ServiceError("Erro ao buscar estatísticas de disponibilidade") from e