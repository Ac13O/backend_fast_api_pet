from fastapi import APIRouter

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/ping_app")
async def ping_app():
    return {"ping_app": "OK"}


@router.get("/ping_db")
async def ping_db():
    return {"ping_db": "OK"}
