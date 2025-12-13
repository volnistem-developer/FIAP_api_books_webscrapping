from fastapi import APIRouter, Depends, HTTPException

from src.api.configuration.dependency_injection_config import services
from src.api.middlewares.auth_middleware import ProtectedRoute
from src.api.configuration.protected_security_decorator import protected

from src.dtos.user_dto import UserCreateDTO, UserIdDTO, UserReadDTO, UserUpdateDTO

router = APIRouter(prefix="/api/v1/users", tags=["User"], route_class=ProtectedRoute)


@router.get("/", status_code=200, response_model=list[UserReadDTO])
@protected()
def list_all_users():

    retorno = services.user_service.list_all()

    if len(services.user_service.validation) > 0:   
        ex = services.user_service.validation[0]   

        raise HTTPException(status_code=ex.status_code, detail=ex.message)

    return retorno

@router.get("/{id}", status_code=200, response_model=UserReadDTO)
@protected()
def get_user_by_id(params: UserIdDTO = Depends()):
    role_id = params.id

    retorno = services.user_service.get_by_id(role_id)

    if len(services.user_service.validation) > 0:   
        ex = services.user_service.validation[0]   

        raise HTTPException(status_code=ex.status_code, detail=ex.message)

    return retorno

@router.post("/", response_model=UserReadDTO , status_code=201)
def insert_user(user: UserCreateDTO):

    retorno = services.user_service.insert_user(user)

    if len(services.user_service.validation) > 0:   
        ex = services.user_service.validation[0]   

        raise HTTPException(status_code=ex.status_code, detail=ex.message)

    return retorno

@router.delete("/{id}", status_code=204)
@protected()
def delete_user(params: UserIdDTO = Depends()):
    role_id = params.id

    services.user_service.delete_user(role_id)

    if len(services.user_service.validation) > 0:   
        ex = services.user_service.validation[0]   

        raise HTTPException(status_code=ex.status_code, detail=ex.message)

    return

@router.put("/{id}", status_code=200, response_model=UserReadDTO)
@protected()
def update_user(id:int, user: UserUpdateDTO):

    retorno = services.user_service.update_user(id, user)

    if len(services.user_service.validation) > 0:   
        ex = services.user_service.validation[0]   

        raise HTTPException(status_code=ex.status_code, detail=ex.message)

    return retorno
