from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.dados.database.base import Base

DATABASE_URL = "sqlite:///storage.db"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


class Database:
    def __enter__(self) -> Session:
        self.session = SessionLocal()
        return self.session

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()
