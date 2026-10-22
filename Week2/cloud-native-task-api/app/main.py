
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Cloud-Native Task API",
    description="A simple REST API for managing tasks.",
    version="1.0.0",
)


class TaskCreate(BaseModel):
    title: str


class Task(TaskCreate):
    id: int
    completed: bool = False


tasks: dict[int, Task] = {}
next_id = 1


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    return list(tasks.values())


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_data: TaskCreate):
    global next_id

    task = Task(
        id=next_id,
        title=task_data.title,
        completed=False,
    )
    tasks[next_id] = task
    next_id += 1
    return task


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
