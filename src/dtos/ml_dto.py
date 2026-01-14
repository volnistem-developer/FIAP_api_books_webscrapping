from pydantic import BaseModel


class MLFeaturesDTO(BaseModel):
    book_id: int
    rating: float
    price_brl: float
    available: int
    num_categories: int

class MLTrainingDTO(MLFeaturesDTO):
    target: int