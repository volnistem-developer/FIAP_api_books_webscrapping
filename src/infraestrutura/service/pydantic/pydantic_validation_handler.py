from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from src.infraestrutura.service.pydantic.pydantic_translate_messages import PydanticErrorsPT


def translate_message(type_: str, ctx: dict | None) -> str:
    ctx = ctx or {}

    template = PydanticErrorsPT.get(type_)

    if not template:
        return "valor inválido"

    return template.format(**ctx)


async def pydantic_validation_handler(request: Request, exc: RequestValidationError):
    errors = []

    for erro in exc.errors():
        local = erro["loc"]

        if local and local[0] == "body" or local[0] == "path":
            local = local[1:]

        field = ".".join(str(x) for x in local)

        message = translate_message(erro["type"], erro.get("ctx"))

        errors.append({field: message})

    return JSONResponse(status_code=400, content={"erros": errors})
