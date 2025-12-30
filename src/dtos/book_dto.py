from pydantic import BaseModel, Field

from src.dtos.category_dto import CategoryReadDTO

class BookIdDTO(BaseModel):
    id: int = Field(gt=0)

class BookReadDTO(BaseModel):
    id: int
    title: str 
    slug: str
    rating: int
    raw_price_in_cents: int
    raw_price: float
    brl_price_in_cents: int
    brl_price: float
    image_path: str
    available: bool
    categories: list[CategoryReadDTO]

class CatalogBooksDTO(BaseModel):    
    page: int
    page_size: int
    total_of_books: int
    total_of_pages: int
    catalog: list[BookReadDTO]