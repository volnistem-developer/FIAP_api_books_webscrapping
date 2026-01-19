
from fastapi import APIRouter

from src.api.config.dependency_injection_config import services
from src.api.middlewares.auth_middleware import ProtectedRoute
from src.dtos.ml_dto import MLFeaturesDTO, MLTrainingDTO


router = APIRouter(prefix="/api/v1/ml", tags=["ML"], route_class=ProtectedRoute)

@router.get("/features", status_code=200, response_model=list[MLFeaturesDTO])
def features():
    service = services.get_ml_service()

    return service.get_ml_features()

@router.get("/training-data", status_code=200, response_model=list[MLTrainingDTO])
def training_data():
    service = services.get_ml_service()

    return service.get_training_data()