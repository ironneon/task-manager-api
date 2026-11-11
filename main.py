
from fastapi import FastAPI, status, HTTPException, Depends
from sqlalchemy.orm import Session

from database import Base, engine
from models import Task, User
from schemas import TaskCreate, TaskUpdate, TaskResponse
from auth_routes import router as auth_router
from dependencies import get_db, get_current_user


# Create database tables if they do not exist
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Task Manager API",
    description="ABDMALK PH - Task Manager API with Authentication",
    version="2.0.0"
)

app.include_router(auth_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to ABDMALK PH Task Manager API",
        "status": "running"
    }


@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Task).filter(
        Task.user_id == current_user.id
    ).all()


@app.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED
)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_task = Task(
        title=task.title,
        completed=task.completed,
        user_id=current_user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    existing_task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == current_user.id
    ).first()

    if existing_task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    update_data = task.model_dump(
        exclude_unset=True,
        exclude_none=True
    )

    for key, value in update_data.items():
        setattr(existing_task, key, value)

    db.commit()
    db.refresh(existing_task)

    return existing_task


@app.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    existing_task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == current_user.id
    ).first()

    if existing_task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(existing_task)
    db.commit()

    return {"message": "Task deleted successfully"}
