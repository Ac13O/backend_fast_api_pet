from fastapi import APIRouter

router = APIRouter(prefix="/tasks", tags=["tasks_"])


@router.get("/")
async def simple():
    return []


@router.get("/all")
async def get_tasks():
    return {"tasks": "all"}


@router.post("/task/{taskid}")
async def create_task(taskid):
    return
