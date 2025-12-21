from datetime import datetime
import enum

from sqlalchemy import Column, DateTime, Enum, Integer, Text, func

from src.data.database.base import Base


class EScrapStatus(enum.Enum):
    RUNNING = 'running'
    FINISHED = 'finished'
    ERROR = 'error'

class ScrapEntity(Base):
    __tablename__ = "scraping_execution"

    id = Column(Integer, primary_key=True)
    status = Column(Enum(EScrapStatus), nullable=False)

    started_at = Column(DateTime, nullable=False, server_default=func.now())
    finished_at = Column(DateTime, nullable=True)


    error_message = Column(Text, nullable=True)

    def __init__(self, status: EScrapStatus, started_at: datetime):
        self.status = status
        self.started_at = started_at