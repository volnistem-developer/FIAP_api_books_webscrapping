from typing import List
from src.data.database.unity_of_work import UnityOfWork
from src.entity.category_entity import CategoryEntity
from src.infraestrutura.logging.logger import get_logger
from src.interfaces.application.interface_category_application import ICategoryApplication

class CategoryApplication(ICategoryApplication):
        
    def __init__(self, domain) -> None:
        self.__domain = domain
        self.__logger = get_logger(self.__class__.__name__)

    def list_all_categories(self) -> List[CategoryEntity]:
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