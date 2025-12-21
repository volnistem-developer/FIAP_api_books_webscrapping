from sqlalchemy import Column, ForeignKey, Table

from src.data.database.base import Base


book_categories = Table(
    "book_categories",
    Base.metadata,
    Column("book_id", ForeignKey("books.id"), primary_key=True),
    Column("category_id", ForeignKey("categories.id"), primary_key=True)
)