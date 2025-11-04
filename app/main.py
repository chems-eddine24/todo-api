from fastapi import FastAPI, HTTPException, Depends
from requests import Session
from schemas import *
from typing import Optional
from db import *
from sqlalchemy import create_engine




engine = create_engine(DATABASE_URL)
conn = engine.connect()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI(title="Todo API")


@app.get('/')
def home():
   return {"message":"Welcome to Todo API"}


@app.get('/todos/', response_model=list[TaskR])
def get_all_tasks(db: Session = Depends(get_db)):
   return db.query(Task).all()

@app.post("/todos/", response_model=TaskR)
def create_task(add_task: AddTask, db: Session = Depends(get_db)):
    task = Task(
        title=add_task.title,
        description=add_task.description,
        status=add_task.status,
        Date=add_task.Date
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@app.get('/todos/{task_id}/')
def get_task_by_id(task_id: str, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
@app.patch('/todos/{task_id}/', response_model=TaskR)
def edit_task(task_id: str, edit_task: EditTask, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.title = edit_task.title if edit_task.title is not None else task.title
    task.description = edit_task.description if edit_task.description is not None else task.description
    task.status = edit_task.status if edit_task.status is not None else task.status
    task.Date = edit_task.Date if edit_task.Date is not None else task.Date
    db.commit()
    db.refresh(task)
    return task

@app.delete('/todos/{task_id}/')
def delete_task(task_id: str, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}

@app.get("/todos/search")
def get_todos_by_status_and_title(status: Optional[str] = None, title: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(Task)
    if status:
        query = query.filter(Task.status == status)
    if title:
        query = query.filter(Task.title.contains(title))
    results = query.all()
    if not results:
        raise HTTPException(status_code=404, detail="No tasks found with the given filters")
    return results
 
