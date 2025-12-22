import math
from typing import Dict, List, Optional
from src.dtos.book_dto import BookReadDTO
from src.entity.book_entity import BookEntity
from src.infraestrutura.repository.book_repository import BookRepository


class BookService():

    def __init__(self, application) -> None:
        self.application = application

    def get_all_books(self, page: int = 1, page_size: int = 10) -> Dict:
        
        books, total = self.application.list_all_books(page, page_size)

        return {
            "page": page,
            "page_size": page_size,
            "total_of_books": total,
            "total_of_pages": math.ceil(total / page_size),
            "catalog": [self.__convert_entity_to_dto(e) for e in books],
        }
    
    def get_all_books_most_rated(self, page: int = 1, page_size: int = 10) -> Dict:

        books, total = self.application.get_all_books_most_rated(page, page_size)

        return {
            "page": page,
            "page_size": page_size,
            "total_of_books": total,
            "total_of_pages": math.ceil(total / page_size),
            "catalog": [self.__convert_entity_to_dto(e) for e in books],
        }
    
    def get_book(self, id: int) -> BookReadDTO:

        entity = self.application.get_book(id)

        return self.__convert_entity_to_dto(entity)
    
    def get_books_from_title_or_category(self, title: Optional[str], category: Optional[str]) -> List[BookReadDTO]:
    
        books = self.application.get_books_from_title_or_category(title, category)

        return [self.__convert_entity_to_dto(e) for e in books]

    def get_by_price_range(self, price_min: float, price_max: float) -> List[BookReadDTO]:
        books = self.application.get_by_price_range(price_min, price_max)

        return [self.__convert_entity_to_dto(e) for e in books]

    def __convert_entity_to_dto(self, entity: BookEntity) -> BookReadDTO:
        #libras esterlinas no dia 20/12/2025 - R$7,41 - valor que está no site de scraping está em libras esterilinas
        return BookReadDTO(
            id=entity.id,
            title=entity.title,
            slug=entity.slug,
            rating=entity.rating,
            raw_price_in_cents=entity.raw_price_in_cents,
            raw_price=(entity.raw_price_in_cents/100),
            brl_price_in_cents=int(round((entity.raw_price_in_cents/100)*7.41, 2)*100),
            brl_price=round((entity.raw_price_in_cents/100)*7.41, 2),
            image_path=entity.image_path,
            categories=[{"id": c.id, "name": c.name} for c in entity.categories]
        )