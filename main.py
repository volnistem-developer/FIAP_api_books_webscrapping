from typing import Callable
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse

from src.exceptions.exceptions import (
    AuthenticationFailedError,
    BookScrapingApiError,
    DataError,
    ForbiddenError, 
    IntegrityError, 
    InvalidOperationError,
    InvalidTokenError, 
    ServiceError, 
    EntityDoesNotExistsError,
    UnauthorizedError
)
from src.infraestrutura.config.pydantic.pydantic_validation_handler import pydantic_validation_handler
from src.api.controllers.v1.user_auth_controller import router as user_auth_router
from src.api.controllers.v1.user_controller import router as user_router
from src.api.controllers.v1.scrap_controller import router as scrap_router
from src.api.controllers.v1.book_controller import router as book_router
from src.api.controllers.v1.health_controller import router as health_router
from src.api.controllers.v1.stats_controller import router as stats_router
from src.api.controllers.v1.ml_controller import router as ml_router
from src.data.database.base import Base
from src.data.database.db import engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Books Webscrapping API",
        version="1.0.0",
        description="API para raspagem e entraga de dados para o cliente.",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "Authorization": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }

    openapi_schema["security"] = [
        {"Authorization": []}
    ]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

def include_routes():
    app.include_router(user_auth_router)
    app.include_router(user_router)
    app.include_router(scrap_router)
    app.include_router(book_router)
    app.include_router(health_router)
    app.include_router(stats_router)
    app.include_router(ml_router)

def create_exception_handler(
    status_code: int, initial_detail: str
) -> Callable[[Request, BookScrapingApiError], JSONResponse]:
    detail = {"message": initial_detail}  # Using a dictionary to hold the detail

    async def exception_handler(_: Request, exc: BookScrapingApiError) -> JSONResponse:
        if exc.message:
            detail["message"] = exc.message

        if exc.name:
            detail["message"] = f"{detail['message']}"

        return JSONResponse(
            status_code=status_code, content={"message": detail["message"]}
        )

    return exception_handler

def exception_handler():
    app.add_exception_handler(
    exc_class_or_status_code=EntityDoesNotExistsError,
    handler=create_exception_handler(
        status.HTTP_404_NOT_FOUND, "Entity does not exist."
        ),
    )

    app.add_exception_handler(
        exc_class_or_status_code=InvalidOperationError,
        handler=create_exception_handler(
            status.HTTP_400_BAD_REQUEST, "Não foi possível realizar essa ação."
        ),
    )

    app.add_exception_handler(
        exc_class_or_status_code=IntegrityError,
        handler=create_exception_handler(
            status.HTTP_400_BAD_REQUEST, "Não foi possível processar, devido a um erro de integridade."
        ),
    )

    app.add_exception_handler(
        exc_class_or_status_code=DataError,
        handler=create_exception_handler(
            status.HTTP_400_BAD_REQUEST, "Dados não puderam ser processados, confira os campos."
        ),
    )

    app.add_exception_handler(
        exc_class_or_status_code=AuthenticationFailedError,
        handler=create_exception_handler(
            status.HTTP_401_UNAUTHORIZED,
            "Falha na autenticação, credenciais inválidas.",
        ),
    )

    app.add_exception_handler(
        exc_class_or_status_code=ForbiddenError,
        handler=create_exception_handler(
            status.HTTP_403_FORBIDDEN, "Ação inválida, parece que você não tem permissão para isso."
        ),
    )

    app.add_exception_handler(
        exc_class_or_status_code=InvalidTokenError,
        handler=create_exception_handler(
            status.HTTP_401_UNAUTHORIZED, "Token inválido, por favor faça login novamente."
        ),
    )

    app.add_exception_handler(
        exc_class_or_status_code=UnauthorizedError,
        handler=create_exception_handler(
            status.HTTP_401_UNAUTHORIZED, "Não autorizado"
        ),
    )

    app.add_exception_handler(
        exc_class_or_status_code=ServiceError,
        handler=create_exception_handler(
            status.HTTP_500_INTERNAL_SERVER_ERROR, 'Ocorreu um erro inesperado ao comunicar com servidor, tente novamente.'
        )
    )

include_routes()
exception_handler()

app.openapi = custom_openapi
