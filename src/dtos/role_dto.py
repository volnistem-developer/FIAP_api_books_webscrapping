from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class RoleCreateDTO(BaseModel):
    name: str = Field(min_length=3, max_length=20)


class RoleReadDTO(BaseModel):
    id: int
    name: str
    created_at: datetime
    active: bool

class RoleIdDTO(BaseModel):
    id: int = Field(gt=0)