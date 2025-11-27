from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/v1/users", tags=["User"])


@router.get("/")
def list():
    return {"user"}
