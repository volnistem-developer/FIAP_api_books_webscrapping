from src.data.database.unity_of_work import UnityOfWork
from src.infraestrutura.logging.logger import get_logger
from src.interfaces.application.interface_stats_application import IStatsApplication
from src.interfaces.domain.interface_stats_domain import IStatsDomain

class StatsApplication(IStatsApplication):

    def __init__(self, domain: IStatsDomain) -> None:
        self.__domain = domain
        self.__logger = get_logger(self.__class__.__name__)

    def get_overview(self) -> dict:
        self.__logger.info("Fetching overview statistics")

        with UnityOfWork() as uow:
            try:
                self.__domain.attach_uow(uow)

                result = self.__domain.get_overview()

                self.__logger.info(
                    "Overview statistics fetched successfully",
                    extra={
                        "total_books": result.get("total_books"),
                        "available_books": result.get("available_books"),
                    }
                )

                return result

            except Exception:
                self.__logger.exception("Error while fetching overview statistics")
                raise

    def get_categories_stats(self) -> list[dict]:
        self.__logger.info("Fetching category statistics")

        with UnityOfWork() as uow:
            try:
                self.__domain.attach_uow(uow)

                result = self.__domain.get_categories_stats()

                self.__logger.info(
                    f"Category statistics fetched successfully ({len(result)} categories)"
                )

                return result

            except Exception:
                self.__logger.exception("Error while fetching category statistics")
                raise

    def get_availability_stats(self) -> dict:
        self.__logger.info("Fetching availability statistics")

        with UnityOfWork() as uow:
            try:
                self.__domain.attach_uow(uow)

                result = self.__domain.get_availability_stats()

                self.__logger.info(
                    "Availability statistics fetched successfully",
                    extra=result
                )

                return result

            except Exception:
                self.__logger.exception("Error while fetching availability statistics")
                raise