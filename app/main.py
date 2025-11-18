
from fastapi import FastAPI, HTTPException, Depends, APIRouter
from requests import Session
from app.schemas.schemas_task import *
from app.schemas.schemas_user import *
from typing import Optional
from app.models.db_task import *
from app.db.core import *
from app.models.db_user import *
from app.models.db_task import *
from app.endpoints import tasks, users
from app.endpoints.users import get_password_hash, verify_password
import random
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


app = FastAPI(title="Todo API")
app.include_router(tasks.router)
app.include_router(users.router)


@app.get('/')
def home():
   return {"message":"Welcome to Todo API"}

#User Endpoints
@app.post('/register/', response_model=UserR)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    query = await db.execute(select(User).filter(User.email == user.email))
    existing_user = query.scalars().first()
    if existing_user:
        raise HTTPException(
            detail="User with this email already exists",
            status_code=400
        )
    user = User(
        email=user.email,
        password_hash=get_password_hash(user.password)
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

@app.post('/login/', response_model=Token)
async def login_for_access_token(user: UserCreate, db: AsyncSession = Depends(get_db)):
    query = await db.execute(select(User).filter(User.email == user.email))
    db_user = query.scalars().first()
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
        )
    token = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=50))
    return {"access_token": token, "token_type": "bearer"}
    

@app.get('/todos/', response_model=list[TaskR])
async def get_all_tasks(db: AsyncSession = Depends(get_db)):
   query = await db.execute(select(Task))
   tasks = query.scalars().all()
   return tasks

@app.post("/todos/", response_model=TaskR)
async def create_task(add_task: AddTask, db: AsyncSession = Depends(get_db)):
    query = await db.execute(select(Task).filter(Task.title == add_task.title))
    existing_task = query.scalars().first()
    if existing_task:
        raise HTTPException(
            detail="Task with this title already exists",
            status_code=400
        )
    task = Task(**add_task.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


@app.get('/todos/{task_id}/')
async def get_task_by_id(task_id: str, db: AsyncSession = Depends(get_db)):
    query = await db.execute(select(Task).filter(Task.id == task_id))
    task = query.scalars().first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
@app.patch('/todos/{task_id}/', response_model=TaskR)
async def edit_task(task_id: str, edit_task: EditTask, db: AsyncSession = Depends(get_db)):
    query = await db.execute(select(Task).filter(Task.id == task_id))
    task = query.scalars().first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.title = edit_task.title if edit_task.title is not None else task.title
    task.description = edit_task.description if edit_task.description is not None else task.description
    task.status = edit_task.status if edit_task.status is not None else task.status
    task.Date = edit_task.Date if edit_task.Date is not None else task.Date
    await db.commit()
    await db.refresh(task)
    return task

@app.delete('/todos/{task_id}/')
async def delete_task(task_id: str, db: AsyncSession = Depends(get_db)):
    query = await db.execute(select(Task).filter(Task.id == task_id))
    task = query.scalars().first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    await db.delete(task)
    await db.commit()
    return {"message": "Task deleted successfully"}

@app.get("/todos/search")
async def get_todos_by_status_and_title(status: Optional[str] = None, title: Optional[str] = None, db: AsyncSession = Depends(get_db)):
    query = db.execute(select(Task))
    if status:
        query = query.filter(Task.status == status)
    if title:
        query = query.filter(Task.title.contains(title))
    results = await query.scalars().all()
    if not results:
        raise HTTPException(status_code=404, detail="No tasks found with the given filters")
    return results
 

