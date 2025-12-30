from datetime import datetime
from pydantic import BaseModel


class OverviewDTO(BaseModel):
    total_books: int
    available_books: int
    unavailable_books: int
    average_rating: float
    average_price_brl: float
    last_scrap_execution: datetime

class CategoryStatsDTO(BaseModel):
    category: str
    total_books: int
    available_books: int
    average_rating: float
    average_price_brl: float

class AvailabilityStatsDTO(BaseModel):
    total_books: int
    available_books: int
    unavailable_books: int
    availability_rate: float