from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from src.anticorrupcao.traducao.pydantic_translate_messages import PydanticErrorsPT


def traduzir_msg(type_: str, ctx: dict | None) -> str:
    ctx = ctx or {}

    template = PydanticErrorsPT.get(type_)

    if not template:
        return "valor inválido"

    return template.format(**ctx)


async def pydantic_validation_handler(request: Request, exc: RequestValidationError):
    erros = []

    for erro in exc.errors():
        local = erro["loc"]

        if local and local[0] == "body" or local[0] == "path":
            local = local[1:]

        campo = ".".join(str(x) for x in local)

        mensagem = traduzir_msg(erro["type"], erro.get("ctx"))

        erros.append({campo: mensagem})

    return JSONResponse(status_code=400, content={"erros": erros})
