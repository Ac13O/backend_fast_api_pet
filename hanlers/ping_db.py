from fastapi import APIRouter

router = APIRouter(prefix="/ping", tags=["ping_"])


@router.get("/ping_app")
async def ping_app():
    return {"ping_app": "OK"}


@router.get("/ping_db")
async def ping_db():
    return {"ping_db": "OK"}
