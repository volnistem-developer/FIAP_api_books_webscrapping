from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.utils import get_openapi

from src.infraestrutura.service.pydantic.pydantic_validation_handler import pydantic_validation_handler
from src.api.controllers.v1.user_controller import router as user_router
from src.api.controllers.v1.user_auth_controller import router as user_auth_router
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

    # remove 422 globalmente
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method.get("responses", {}).pop("422", None)

    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.include_router(user_router)
app.include_router(user_auth_router)

app.add_exception_handler(RequestValidationError, pydantic_validation_handler)

app.openapi = custom_openapi
