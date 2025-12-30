from datetime import datetime
from fastapi import APIRouter
from sqlalchemy import text

from src.data.database.unity_of_work import UnityOfWork


router = APIRouter(prefix="/api/v1/health", tags=["Health"])

@router.get("/", status_code=200)
def health_check():
    try:
        with UnityOfWork() as uow:
            uow.session.execute(text("SELECT 1"))

        return {
            "status": "ok",
            "api": "up",
            "database": "up",
            "timestamp": datetime.utcnow().isoformat()
        }

    except Exception as e:
        print(e)
        return {
            "status": "error",
            "api": "up",
            "database": "down",
            "error": str(e),
            "timestamp": datetime.utcnow().isoformat()
        }