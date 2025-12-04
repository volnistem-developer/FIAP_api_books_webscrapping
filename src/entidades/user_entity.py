from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String, ForeignKey

from src.dados.database.base import Base

class UserEntity(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=False)
    active = Column(Boolean, nullable=False, default=True)

    def __init__(
        self, name: str, username: str, email: str, password: str, created_at: datetime = datetime.now(), active: bool = True
    ) -> None:
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.created_at = created_at
        self.active = active