from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.dados.database.base import Base


class Database:
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage.db"
        self.__engine = None
        self.__session = None

    def connect(self):
        self.__engine = create_engine(self.__connection_string)

        Base.metadata.create_all(self.__engine)

    def __enter__(self):
        session_maker = sessionmaker()
        self.__session = session_maker(bind=self.__engine)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.__session is not None:
            self.__session.close


db_connection_handler = Database()
