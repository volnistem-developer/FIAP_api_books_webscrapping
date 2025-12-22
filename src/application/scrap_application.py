from src.infraestrutura.logging.logger import get_logger
from src.data.database.unity_of_work import UnityOfWork
from src.interfaces.application.interface_scrap_application import IScrapApplication
from src.interfaces.domain.interface_scrap_domain import IScrapDomain


class ScrapApplication(IScrapApplication):

    def __init__(self, domain: IScrapDomain, anticorruption) -> None:
        self.__domain = domain
        self.__anticorruption = anticorruption
        self.__logger = get_logger(self.__class__.__name__)

    def start_scraping(self):
        self.__logger.info("Scraping process started")

        with UnityOfWork() as uow:
            try:
                self.__domain.attach_uow(uow)

                self.__logger.info("Checking if scraping can start")
                self.__domain.can_start_scraping()

                job = self.__domain.create_execution()
                self.__logger.info(f"Scraping job created (id={job.id}, status=RUNNING)")

                # Commit imediato para visibilidade do status RUNNING
                uow.commit()
                self.__logger.info("Scraping job persisted with status RUNNING")

                categories = self.__anticorruption.get_categories()
                self.__logger.info(f"{len(categories)} categories found")

                for idx, category in enumerate(categories, start=1):
                    self.__logger.info(
                        f"Processing category {idx}/{len(categories)}: {category['name']}"
                    )

                    books = self.__anticorruption.get_books_from_category(category)
                    self.__logger.info(
                        f"{len(books)} books found in category '{category['name']}'"
                    )

                    self.__domain.save_category_with_books(category, books)

                self.__domain.mark_finished(job)
                self.__logger.info(
                    f"Scraping finished successfully (job_id={job.id})"
                )

            except Exception as e:
                self.__logger.exception("Scraping failed with unexpected error")
                self.__domain.mark_error(job, e)
                raise

    def get_status(self) -> dict:
        self.__logger.info("Fetching scraping status")

        with UnityOfWork() as uow:
            try:
                self.__domain.attach_uow(uow)

                last = self.__domain.get_last_execution()

                if not last:
                    self.__logger.info("No scraping execution found")
                    return {"message": "never_executed"}

                self.__logger.info(
                    f"Last scraping status: {last.status.value}"
                )

                return {
                    "status": last.status.value,
                    "started_at": last.started_at,
                    "finished_at": last.finished_at,
                    "error": last.error_message,
                }

            except Exception:
                self.__logger.exception("Error while fetching scraping status")
                raise