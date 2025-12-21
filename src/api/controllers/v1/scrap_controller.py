from fastapi import APIRouter, BackgroundTasks

from src.api.config.dependency_injection_config import services
from src.api.config.protected_security_decorator import protected
from src.api.middlewares.auth_middleware import ProtectedRoute

router = APIRouter(prefix="/api/v1/scraping", tags=["Scraping"], route_class=ProtectedRoute)

@router.post("/trigger")
@protected()
def trigger_scraping(background_tasks: BackgroundTasks):

    service = services.get_scrap_service()

    background_tasks.add_task(service.start_scraping)

    return {
        "status": 'scraping started',
        "message": 'scraping running in background'
    }

@router.get("/status")
@protected()
def get_scraping_status():
    service = services.get_scrap_service()

    return service.get_status()