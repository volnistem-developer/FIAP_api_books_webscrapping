
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.data.database.base import Base

from src.entity.book_category import book_categories


class CategoryEntity(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)

    books = relationship(
        "BookEntity",
        secondary=book_categories,
        back_populates="categories"
    )

    def __init__(self, name):
        self.name = name