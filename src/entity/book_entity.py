from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.data.database.base import Base

from src.entity.book_category import book_categories


class BookEntity(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    slug = Column(String(100), unique=True, nullable=False)
    rating = Column(Integer, nullable=False)
    raw_price_in_cents = Column(Integer)
    image_path = Column(String(150))


    categories = relationship(
        "CategoryEntity",
        secondary=book_categories,
        back_populates="books"
    )

    def __init__(self, title, slug, rating, raw_price_in_cents, image_path):
        self.title = title
        self.slug = slug
        self.rating = rating
        self.raw_price_in_cents = raw_price_in_cents
        self.image_path = image_path