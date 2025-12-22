from src.data.database.unity_of_work import UnityOfWork
from src.infraestrutura.logging.logger import get_logger

class CategoryApplication:
        
    def __init__(self, domain) -> None:
        self.__domain = domain
        self.__logger = get_logger(self.__class__.__name__)

    def list_all_categories(self):
        self.__logger.info("Listing all categories")

        with UnityOfWork() as uow:
            try:
                self.__domain.attach_uow(uow)
                categories = self.__domain.list_all_categories()

                self.__logger.info(
                    f"{len(categories)} categories found"
                )
                return categories

            except Exception:
                self.__logger.exception("Error while listing categories")
                raise