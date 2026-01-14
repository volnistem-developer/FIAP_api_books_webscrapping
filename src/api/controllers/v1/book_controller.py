from fastapi import APIRouter, Depends, HTTPException, Query

from src.api.config.dependency_injection_config import services
from src.api.config.protected_security_decorator import protected
from src.api.middlewares.auth_middleware import ProtectedRoute
from src.dtos.book_dto import BookIdDTO, BookReadDTO, CatalogBooksDTO
from src.dtos.category_dto import CategoryReadDTO

router = APIRouter(prefix="/api/v1/books", tags=["Books"], route_class=ProtectedRoute)


@router.get("/", status_code=200, response_model=CatalogBooksDTO)
@protected()
def list_all_books(page: int = 1, page_size: int = 10):
    service = services.book_service()

    return service.get_all_books(page, page_size)

@router.get("/search", status_code=200, response_model=list[BookReadDTO])
@protected()
def list_books_from_title_or_category(title: str | None = None, category: str | None = None):
    service = services.book_service()

    return service.get_books_from_title_or_category(title, category)

@router.get("/price-range", status_code=200, response_model=list[BookReadDTO])
@protected()
def get_by_price_range(min: float, max: float):
    service = services.book_service()

    return service.get_by_price_range(min, max)

@router.get("/categories", status_code=200, response_model=list[CategoryReadDTO])
@protected()
def list_all_categories():
    service = services.category_service()

    return service.list_all_categories()

@router.get("/top-rated", status_code=200, response_model=CatalogBooksDTO)
@protected()
def get_top_rated_books(page: int = 1, page_size: int = 10):
    service = services.book_service()

    return service.get_all_books_most_rated()

@router.get("/{id}", status_code=200, response_model=BookReadDTO)
@protected()
def get_book(params: BookIdDTO = Depends()):
    service = services.book_service()

    book_id = params.id

    return service.get_book(book_id)