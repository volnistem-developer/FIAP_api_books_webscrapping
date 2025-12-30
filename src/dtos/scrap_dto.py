from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ScrapStatusDTO(BaseModel):
    status: str
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    error: Optional[str] = None