from fastapi import APIRouter, Depends, HTTPException

from src.api.middlewares.auth_middleware import ProtectedRoute
from src.api.security.decorators import protected

from src.api.service.user_service import ServiceUser
from src.dtos.user_dto import UserCreateDTO, UserIdDTO, UserReadDTO, UserUpdateDTO

router = APIRouter(prefix="/api/v1/users", tags=["User"], route_class=ProtectedRoute)


@router.get("/", status_code=200, response_model=list[UserReadDTO])
@protected()
def list_all_users():
    service = ServiceUser()

    retorno = service.list_all()

    if service.has_exceptions():
        erros = service.get_exceptions()

        erro = erros[0]

        raise HTTPException(status_code=erro.status_code, detail=erro.message)

    return retorno

@router.get("/{id}", status_code=200, response_model=UserReadDTO)
@protected()
def get_user_by_id(params: UserIdDTO = Depends()):
    role_id = params.id

    service = ServiceUser()
    retorno = service.get_by_id(role_id)

    if(service.has_exceptions()):
        erro = service.get_exceptions()[0]

        raise HTTPException(status_code=erro.status_code, detail=erro.message)
    
    return retorno

@router.post("/", response_model=UserReadDTO , status_code=201)
def insert_user(user: UserCreateDTO):
    service = ServiceUser()

    retorno = service.insert_user(user)

    if service.has_exceptions():
        erros = service.get_exceptions()

        erro = erros[0]

        raise HTTPException(status_code=erro.status_code, detail=erro.message)

    return retorno

@router.delete("/{id}", status_code=204)
@protected()
def delete_user(params: UserIdDTO = Depends()):
    role_id = params.id

    service = ServiceUser()
    service.delete_user(role_id)

    if(service.has_exceptions()):
        erro = service.get_exceptions()[0]

        raise HTTPException(status_code=erro.status_code, detail=erro.message)
    
    return 

@router.put("/{id}", status_code=200, response_model=UserReadDTO)
@protected()
def update_user(id:int, user: UserUpdateDTO):

    service = ServiceUser()
    retorno = service.update_user(id, user)

    if(service.has_exceptions()):
        erro = service.get_exceptions()[0]

        raise HTTPException(status_code=erro.status_code, detail=erro.message)
    
    return retorno
