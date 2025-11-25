from fastapi import FastAPI

from src.api.controllers.v1.role_controller import router
from src.dados.database.db import db_connection_handler

app = FastAPI()

db_connection_handler.connect()

app.include_router(router)
