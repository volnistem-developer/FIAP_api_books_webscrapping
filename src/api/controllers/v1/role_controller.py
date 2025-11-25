from fastapi import APIRouter

router = APIRouter(prefix="/v1/roles")


class RoleController:
    @router.get("/")
    def list():
        return {"teste"}
