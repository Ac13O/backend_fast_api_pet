from fastapi import APIRouter, status
from fixtures import tasks as fixture_tasks
from schema.task import Task

router = APIRouter(prefix="/task", tags=["tasks_"])


@router.get("/all", response_model=list[Task])
async def get_tasks():
    return fixture_tasks


@router.post("/", response_model=Task)
async def create_task(task: Task):
    fixture_tasks.append(task)
    return task


@router.patch("/{task_id}", response_model=Task)
async def update_task(task_id: int, new_name: str):
    for task in fixture_tasks:
        if task.get("id") == task_id:
            task.update({"name": new_name})
            return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    for task in fixture_tasks:
        if task.get("id") == task_id:
            fixture_tasks.remove(task)
            return f"Task with id = {task_id} was removed"
    return "Task was not found"
