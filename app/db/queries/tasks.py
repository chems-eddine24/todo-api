from app.db.core import *
from app.models.db_task import *
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.schemas_task import AddTask, TaskR, EditTask



async def get_all_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()

async def create_task(add_task: AddTask, db: Session = Depends(get_db)):
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

async def get_task_by_id(task_id: str, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
async def edit_task(task_id: str, edit_task: EditTask, db: Session = Depends(get_db)):
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

async def delete_task(task_id: str, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}