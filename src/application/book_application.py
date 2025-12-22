from typing import List
from src.data.database.unity_of_work import UnityOfWork
from src.entity.book_entity import BookEntity


from src.infraestrutura.logging.logger import get_logger
from src.interfaces.application.interface_book_application import IBookApplication

class BookApplication(IBookApplication):

    def __init__(self, domain) -> None:
        self.__domain = domain
        self.__logger = get_logger(self.__class__.__name__)

    def list_all_books(self, page: int, page_size: int) -> List[BookEntity]:
        self.__logger.info(
            f"Listing books (page={page}, page_size={page_size})"
        )

        with UnityOfWork() as uow:
            try:
                self.__domain.attach_uow(uow)
                result = self.__domain.list_all_books(page, page_size)

                self.__logger.info(
                    "Books listed successfully"
                )
                return result

            except Exception:
                self.__logger.exception(
                    "Error while listing books"
                )
                raise
        
    def get_all_books_most_rated(self, page: int, page_size: int) -> List[BookEntity]:
        self.__logger.info(
            f"Listing most rated books (page={page}, page_size={page_size})"
        )

        with UnityOfWork() as uow:
            try:
                self.__domain.attach_uow(uow)
                result = self.__domain.get_all_books_most_rated(page, page_size)

                self.__logger.info(
                    "Most rated books listed successfully"
                )
                return result

            except Exception:
                self.__logger.exception(
                    "Error while listing most rated books"
                )
                raise
        
    def get_book(self, id: int) -> BookEntity:
        self.__logger.info(f"Fetching book by id={id}")

        with UnityOfWork() as uow:
            try:
                self.__domain.attach_uow(uow)
                book = self.__domain.get_book(id)

                self.__logger.info(f"Book found (id={id})")
                return book

            except Exception:
                self.__logger.exception(f"Error while fetching book (id={id})")
                raise
        
    def get_by_price_range(self, price_min: float, price_max: float) -> List[BookEntity]:
        self.__logger.info(
            f"Fetching books by price range (min={price_min}, max={price_max})"
        )

        with UnityOfWork() as uow:
            try:
                self.__domain.attach_uow(uow)
                books = self.__domain.get_by_price_range(price_min, price_max)

                self.__logger.info(
                    f"Books fetched by price range (min={price_min}, max={price_max})"
                )
                return books

            except Exception:
                self.__logger.exception(
                    "Error while fetching books by price range"
                )
                raise
        
    def get_books_from_title_or_category(self, title: str | None, category: str | None) -> List[BookEntity]:
        self.__logger.info(
            f"Searching books (title={title}, category={category})"
        )

        with UnityOfWork() as uow:
            try:
                self.__domain.attach_uow(uow)
                books = self.__domain.get_books_from_title_or_category(
                    title, category
                )

                self.__logger.info(
                    "Books search completed successfully"
                )
                return books

            except Exception:
                self.__logger.exception(
                    "Error while searching books by title or category"
                )
                raise
