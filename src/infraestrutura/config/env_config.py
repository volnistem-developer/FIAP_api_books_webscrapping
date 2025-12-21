import os

ENV_CONFIG = {
    "JWT_SECRET": os.getenv('JWT_SECRET_KEY'),
    "JWT_ALGORITHM": os.getenv('JWT_ALGORITHM'),
    "DB_STRING_PATH": os.getenv('DB_PATH'),
    "URL_TO_SCRAPE": os.getenv('URL_TO_SCRAPE'),
    "SCRAPING_COOLDOWN_MINUTES": os.getenv("SCRAPING_COOLDOWN_MINUTES")
}