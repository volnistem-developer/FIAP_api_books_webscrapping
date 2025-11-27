from fastapi import APIRouter, HTTPException, Depends

from src.api.service.role_service import ServiceRole
from src.dtos.role_dto import RoleCreateDTO, RoleReadDTO, RoleIdDTO

router = APIRouter(prefix="/v1/roles", tags=["Role"])


@router.get("/", status_code=200, response_model=list[RoleReadDTO])
def list_all_roles():
    service = ServiceRole()
    retorno = service.list_all()

    if service.has_exceptions():
        erros = service.get_exceptions()

        erro = erros[0]

        raise HTTPException(status_code=erro.status_code, detail=erro.message)

    return retorno

@router.get("/{id}", status_code=200, response_model=RoleReadDTO)
def get_role_by_id(params: RoleIdDTO = Depends()):
    role_id = params.id

    service = ServiceRole()
    retorno = service.get_by_id(role_id)

    if(service.has_exceptions()):
        erro = service.get_exceptions()[0]

        raise HTTPException(status_code=erro.status_code, detail=erro.message)
    
    return retorno

@router.delete("/{id}", status_code=204)
def delete_role(params: RoleIdDTO = Depends()):
    role_id = params.id

    service = ServiceRole()
    service.delete_role(role_id)

    if(service.has_exceptions()):
        erro = service.get_exceptions()[0]

        raise HTTPException(status_code=erro.status_code, detail=erro.message)
    
    return 

@router.put("/{id}", status_code=200, response_model=RoleReadDTO)
def update_role(id:int, role: RoleCreateDTO):

    service = ServiceRole()
    retorno = service.update_role(id, role)

    if(service.has_exceptions()):
        erro = service.get_exceptions()[0]

        raise HTTPException(status_code=erro.status_code, detail=erro.message)
    
    return retorno


@router.post("/", response_model=RoleReadDTO , status_code=201)
def insert_role(role: RoleCreateDTO):
    service = ServiceRole()

    retorno = service.insert_role(role)

    if service.has_exceptions():
        erros = service.get_exceptions()

        erro = erros[0]

        raise HTTPException(status_code=erro.status_code, detail=erro.message)

    return retorno
