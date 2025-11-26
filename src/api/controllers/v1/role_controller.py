from fastapi import APIRouter, Depends

from src.api.service.role_service import ServiceRole
from src.interfaces.service.service_role_interface import IServiceRole

router = APIRouter(prefix="/v1/roles")


class RoleController:
    @router.get("/")
    def list():
        service = ServiceRole()

        return service.list_all()
