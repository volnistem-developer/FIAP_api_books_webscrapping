from src.dtos.ml_dto import MLFeaturesDTO, MLTrainingDTO


class MLService():    
    
    def __init__(self, application) -> None:
        self.application = application


    def get_ml_features(self):
        rows = self.application.get_ml_features()

        return [
            MLFeaturesDTO(
                book_id=r.id,
                rating=r.rating or 0,
                price_brl=round((r.raw_price_in_cents or 0) / 100 * 7.41, 2),
                available=1 if r.available else 0,
                num_categories=r.num_categories
            )
            for r in rows
        ]

    def get_training_data(self):
        rows = self.application.get_ml_training_data()

        return [
            MLTrainingDTO(
                book_id=r.id,
                rating=r.rating or 0,
                price_brl=round((r.raw_price_in_cents or 0) / 100 * 7.41, 2),
                available=1 if r.available else 0,
                num_categories=r.num_categories,
                target=r.target
            )
            for r in rows
        ]