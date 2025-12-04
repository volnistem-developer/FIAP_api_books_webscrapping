from datetime import datetime
from pydantic import BaseModel, Field, EmailStr

class UserCreateDTO(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    username: str = Field(min_length=3, max_length=20)
    email: EmailStr = Field(default=None)
    password: str = Field(min_length=4, max_length=10)


class UserReadDTO(BaseModel):
    id: int
    name: str
    username: str
    email: str
    created_at: datetime
    active: bool

class UserIdDTO(BaseModel):
    id: int = Field(gt=0)

class UserUpdateDTO(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    username: str = Field(min_length=3, max_length=20)
    email: EmailStr = Field(default=None)
    