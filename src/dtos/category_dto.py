from pydantic import BaseModel

class CategoryReadDTO(BaseModel):
    id: int
    name: str