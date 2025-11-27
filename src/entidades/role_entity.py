from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String

from src.dados.database.base import Base


class RoleEntity(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), unique=True, nullable=False)
    created_at = Column(DateTime, nullable=False)
    active = Column(Boolean, default=True, nullable=False)

    def __init__(
        self, name: str, created_at: datetime = datetime.now(), active: bool = True
    ) -> None:
        self.name = name
        self.created_at = created_at
        self.active = active
