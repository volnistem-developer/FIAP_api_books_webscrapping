import os

ENV_CONFIG = {
    "JWT_SECRET": os.getenv('JWT_SECRET_KEY'),
    "JWT_ALGORITHM": os.getenv('JWT_ALGORITHM'),
    "DB_STRING_PATH": os.getenv('DB_PATH')
}