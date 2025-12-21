from src.data.database.unity_of_work import UnityOfWork
from src.entity.book_entity import BookEntity


class BookApplication():

    def __init__(self, domain) -> None:
        self.__domain = domain

    def list_all_books(self, page:int, page_size:int) -> list[BookEntity]:
        with UnityOfWork() as uow:
            self.__domain.attach_uow(uow)
            return self.__domain.list_all_books(page, page_size)
        
    def get_all_books_most_rated(self, page:int, page_size:int) -> list[BookEntity]:
        with UnityOfWork() as uow:
            self.__domain.attach_uow(uow)
            return self.__domain.get_all_books_most_rated(page, page_size)
        
    def get_book(self, id: int) -> BookEntity:
        with UnityOfWork() as uow:
            self.__domain.attach_uow(uow)
            return self.__domain.get_book(id)
        
    def get_by_price_range(self, price_min: float, price_max: float) -> BookEntity:
        with UnityOfWork() as uow:
            self.__domain.attach_uow(uow)
            return self.__domain.get_by_price_range(price_min, price_max)
        
    def get_books_from_title_or_category(self, title: str | None, category: str | None):
        with UnityOfWork() as uow:
            self.__domain.attach_uow(uow)
            return self.__domain.get_books_from_title_or_category(title, category)