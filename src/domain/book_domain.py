from src.data.database.unity_of_work import UnityOfWork
from src.entity.book_entity import BookEntity
from src.exceptions.exceptions import ServiceError


class BookDomain():

    def __init__(self, repository):
        self.__repository = repository

    def attach_uow(self, uow: UnityOfWork):
        self.__repository.uow = uow

    def list_all_books(self, page:int, page_size:int) -> list[BookEntity]:
        try:
            return self.__repository.get_all_books(page, page_size)
        except Exception as e:
            raise ServiceError() from e
        
    def get_all_books_most_rated(self, page:int, page_size:int) -> list[BookEntity]:
        try:
            return self.__repository.get_all_books_most_rated(page, page_size)
        except Exception as e:
            raise ServiceError() from e
        
    def get_book(self, id:int) -> BookEntity:
        try:
            return self.__repository.get_book(id)
        except Exception as e:
            raise ServiceError() from e
        
    def get_by_price_range(self, price_min: float, price_max: float):
        try:
            return self.__repository.get_by_price_range(price_min, price_max)
        except Exception as e:
            raise ServiceError() from e
        
    def get_books_from_title_or_category(self, title: str | None, category: str | None):
        try:
            return self.__repository.get_books_from_title_or_category(title, category)
        except Exception as e:
            raise ServiceError() from e