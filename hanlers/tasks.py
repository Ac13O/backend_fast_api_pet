from fastapi import APIRouter, status

from database import get_db_connection
from schema.task import Task

router = APIRouter(prefix="/task", tags=["tasks_"])


@router.get("/all", response_model=list[Task])
async def get_tasks():
    result = []
    connection = get_db_connection()
    cursor = connection.cursor()
    tasks = cursor.execute("SELECT * FROM Tasks").fetchall()
    for task in tasks:
        result.append(Task(
            id=task[0],
            name=task[1],
            pomodoro_count=task[2],
            category_id=task[3]
        ))
    connection.close()
    return result


@router.post("/", response_model=Task)
async def create_task(task: Task):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Tasks (name, pomodoro_count, category_id) VALUES (?, ?, ?)",
                   (task.name, task.pomodoro_count, task.category_id))
    connection.commit()
    connection.close()
    return task


@router.patch("/{task_id}", response_model=Task)
async def update_task_name(task_id: int, new_name: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE Tasks SET name=? WHERE id=?",
                   (new_name, task_id))
    connection.commit()
    task = cursor.execute("SELECT * FROM Tasks WHERE id=?", f"{task_id}").fetchall()[0]
    connection.close()
    return Task(id=task[0], name=task[1], pomodoro_count=task[2], category_id=task[3])


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Tasks WHERE id=(?)", (str(task_id)))
    connection.commit()
    connection.close()
    return "Task was not found"
