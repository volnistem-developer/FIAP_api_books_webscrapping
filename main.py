from fastapi import FastAPI

from src.api.controllers.v1.role_controller import router
from src.dados.database.base import Base
from src.dados.database.db import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)
