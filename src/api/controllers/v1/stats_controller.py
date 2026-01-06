from fastapi import APIRouter

from src.api.config.dependency_injection_config import services
from src.api.middlewares.auth_middleware import ProtectedRoute
from src.dtos.stats_dto import AvailabilityStatsDTO, CategoryStatsDTO, OverviewDTO


router = APIRouter(prefix="/api/v1/stats", tags=["Statistics"], route_class=ProtectedRoute)

@router.get('/overview', response_model=OverviewDTO, status_code=200)
def overview():
    service = services.get_stats_service()

    return service.get_overview()

@router.get('/categories', response_model=list[CategoryStatsDTO], status_code=200)
def categories_stats():
    service = services.get_stats_service()

    return service.get_categories_stats()

@router.get("/availability", response_model=AvailabilityStatsDTO, status_code=200)
def get_availability_stats():
    service = services.get_stats_service()

    return service.get_availability_stats()