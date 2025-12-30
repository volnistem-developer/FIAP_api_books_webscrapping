from decimal import ROUND_HALF_UP, Decimal
from typing import List, Optional, Tuple
from sqlalchemy import or_, func, case
from sqlalchemy.orm import selectinload

from src.data.database.unity_of_work import UnityOfWork
from src.entity.book_entity import BookEntity
from src.entity.category_entity import CategoryEntity
from src.interfaces.infrastructure.interface_book_repository import IBookRepository


class BookRepository(IBookRepository):

    def __init__(self, uow: UnityOfWork):
        self.uow = uow

    def get_or_create(self, book: dict) -> BookEntity:
        entity = (
            self.uow.session
            .query(BookEntity)
            .filter(BookEntity.slug == book["slug"])
            .one_or_none()
        )

        if entity:
            return entity

        entity = BookEntity(
            title=book["name"],
            slug=book["slug"],
            rating=book["rating"],
            raw_price_in_cents=book["original_price"],
            image_path=book["image_path"],
            available=book["available"]
        )

        self.uow.session.add(entity)
        return entity

    def link_category(self, book: BookEntity, category: CategoryEntity) -> None:
        if category not in book.categories:
            book.categories.append(category)

    def get_all_books(self, page: int, page_size: int) -> Tuple[List[BookEntity], int]:
        offset = (page - 1) * page_size

        entities = (
            self.uow.session
            .query(BookEntity)
            .options(selectinload(BookEntity.categories))
        )

        total = entities.count()

        books = (
            entities.offset(offset).limit(page_size).all()
        )

        return books, total

    def get_all_books_most_rated(self, page: int, page_size: int) -> Tuple[List[BookEntity], int]:

        offset = (page - 1) * page_size

        entities = (
            self.uow.session
            .query(BookEntity)
            .options(selectinload(BookEntity.categories))
            .filter(BookEntity.rating == 5)
        )

        total = entities.count()

        books = (
            entities.offset(offset).limit(page_size).all()
        )

        return books, total
    
    def get_book(self, id: int) -> Optional[BookEntity]:
        
        entity = (
            self.uow.session
            .query(BookEntity)
            .options(selectinload(BookEntity.categories))
            .filter(BookEntity.id == id)
            .one_or_none()
        )

        return entity

    def get_by_price_range(self, price_min: float, price_max: float) -> List[BookEntity]:

        min_cents = int(
            (Decimal(str(price_min)) * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
        )
        
        max_cents = int(
            (Decimal(str(price_max)) * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
        )

        query = (
            self.uow.session
            .query(BookEntity)
            .options(selectinload(BookEntity.categories))
            .filter(BookEntity.raw_price_in_cents.between(min_cents, max_cents))
        )

        return query.all()

    def get_books_from_title_or_category(self, title: Optional[str] = None, category: Optional[str] = None) -> List[BookEntity]:
        query = (
            self.uow.session
            .query(BookEntity)
            .options(selectinload(BookEntity.categories))
        )

        filters = []

        if title:
            filters.append(
                BookEntity.title.ilike(f"%{title}%")
            )
        
        if category:
            filters.append(
                CategoryEntity.name.ilike(f"%{category}%")
            )

            query = query.join(BookEntity.categories)

        if filters:
            query = query.filter(or_(*filters)) 

        return query.distinct().all()
    
    def count_all(self) -> int:
        return self.uow.session.query(func.count(BookEntity.id)).scalar()

    def count_available(self) -> int: 
        return (
            self.uow.session
            .query(func.count(BookEntity.id))
            .filter(BookEntity.available == True)
            .scalar()
        )
    
    def get_average_rating(self) -> float:
        return(
            self.uow.session
            .query(func.avg(BookEntity.rating))
            .scalar() or 0
        )
    
    def get_average_price_brl(self) -> float:
        avg_raw = (
            self.uow.session
            .query(func.avg(BookEntity.raw_price_in_cents))
            .scalar()
        )

        if not avg_raw:
            return 0
        
        return (avg_raw / 100) * 7.41

    def get_stats_by_category(self):
        query = (
            self.uow.session
            .query(
                CategoryEntity.id.label("category_id"),
                CategoryEntity.name.label("category_name"),
                func.count(BookEntity.id).label("total_books"),
                func.sum(
                    case(
                        (BookEntity.available == True, 1), else_=0
                    )
                ).label("available_books"),
                func.avg(BookEntity.rating).label("average_rating"),
                func.avg(BookEntity.raw_price_in_cents).label("average_raw_price_in_cents")
            )
            .join(BookEntity.categories)
            .group_by(CategoryEntity.id, CategoryEntity.name)
        )

        return query.all()
    
    def get_availability_stats(self):
        result = (
            self.uow.session
            .query(
                func.count(BookEntity.id).label("total_books"),
                func.sum(
                    case(
                        (BookEntity.available == True, 1),
                        else_=0
                    )
                ).label("available_books"),
                func.sum(
                    case(
                        (BookEntity.available == False, 1),
                        else_=0
                    )
                ).label("unavailable_books"),
            )
            .one()
        )

        return {
            "total_books": result.total_books or 0,
            "available_books": result.available_books or 0,
            "unavailable_books": result.unavailable_books or 0,
        }