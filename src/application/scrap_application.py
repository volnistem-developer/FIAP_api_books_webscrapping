from src.anticorruption.books_scrape_script import AnticorruptionBooksScraping
from src.data.database.unity_of_work import UnityOfWork
from src.interfaces.application.interface_scrap_application import IScrapApplication
from src.interfaces.domain.interface_scrap_domain import IScrapDomain


class ScrapApplication(IScrapApplication):

    def __init__(self,domain: IScrapDomain, anticorruption) -> None:
        self.__domain = domain
        self.__anticorruption = anticorruption

    def start_scraping(self):
        with UnityOfWork() as uow:
            self.__domain.attach_uow(uow)

            self.__domain.can_start_scraping()

            job = self.__domain.create_execution()

            uow.commit()

            try:
                categories = self.__anticorruption.get_categories()

                for category in categories:
                    books = self.__anticorruption.get_books_from_category(category)
                    self.__domain.save_category_with_books(category, books)

                self.__domain.mark_finished(job)

            except Exception as e:
                self.__domain.mark_error(job, e)
                raise

    def get_status(self) -> dict:
        with UnityOfWork() as uow:
            self.__domain.attach_uow(uow)

            last = self.__domain.get_last_execution()

            if not last:
                return {"message": "never_executed"}

            return {
                "status": last.status,
                "started_at": last.started_at,
                "finished_at": last.finished_at,
                "error": last.error_message,
            }