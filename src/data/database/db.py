from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.infraestrutura.config.env_config import ENV_CONFIG

DATABASE_URL = ENV_CONFIG['DB_STRING_PATH']

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)