from fastapi import APIRouter, Depends, HTTPException

from src.api.config.dependency_injection_config import services
from src.api.middlewares.auth_middleware import ProtectedRoute
from src.api.config.protected_security_decorator import protected

from src.dtos.user_dto import UserCreateDTO, UserIdDTO, UserReadDTO, UserUpdateDTO

router = APIRouter(prefix="/api/v1/users", tags=["User"], route_class=ProtectedRoute)


@router.get("/", status_code=200, response_model=list[UserReadDTO])
@protected()
def list_all_users():
    service, uow = services.user_service()

    with uow:
        return service.list_all()

@router.get("/{id}", status_code=200, response_model=UserReadDTO|None)
@protected()
def get_user_by_id(params: UserIdDTO = Depends()):
    service, uow = services.user_service()

    user_id = params.id

    with uow:
        return service.get_by_id(user_id)

@router.post("/", response_model=UserReadDTO , status_code=201)
def insert_user(user: UserCreateDTO):
    service, uow = services.user_service()

    with uow:
        return service.insert_user(user)

@router.delete("/{id}", status_code=204)
@protected()
def delete_user(params: UserIdDTO = Depends()):
    service, uow = services.user_service()

    user_id = params.id

    with uow:
        return service.delete_user(user_id)

@router.put("/{id}", status_code=200, response_model=UserReadDTO)
@protected()
def update_user(id:int, user: UserUpdateDTO):

    service, uow = services.user_service()

    with uow:
        return service.update_user(id, user)
