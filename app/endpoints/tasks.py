from fastapi import APIRouter, HTTPException, Depends
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.core import get_db
from app.models.db_task import Task
from app.schemas.schemas_task import TaskR, AddTask, EditTask
from app.models.db_user import User
from app.endpoints.auth import get_current_user

router = APIRouter(prefix="/todos", tags=["todos"])


@router.get("/", response_model=list[TaskR])
async def get_all_tasks(current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Task))
    return result.scalars().all()


@router.post("/", response_model=TaskR)
async def create_task(add_task: AddTask, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    task = Task(**add_task.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


@router.get("/{task_id}/", response_model=TaskR)
async def get_task_by_id(task_id: str, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Task).filter(Task.id == task_id))
    task = result.scalar_one_or_none()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@router.patch("/{task_id}/", response_model=TaskR)
async def edit_task(task_id: str, edit_task: EditTask, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Task).filter(Task.id == task_id))
    task = result.scalar_one_or_none()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # update values
    update_data = edit_task.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)

    await db.commit()
    await db.refresh(task)
    return task


@router.delete("/{task_id}/")
async def delete_task(task_id: str, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Task).filter(Task.id == task_id))
    task = result.scalar_one_or_none()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    await db.delete(task)
    await db.commit()
    return {"message": "Task deleted successfully"}


@router.get("/search", response_model=list[TaskR])
async def get_todos_by_status_and_title(
    status: Optional[str] = None,
    title: Optional[str] = None,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    query = select(Task)

    if status:
        query = query.filter(Task.status == status)

    if title:
        query = query.filter(Task.title.contains(title))

    result = await db.execute(query)
    todos = result.scalars().all()

    if not todos:
        raise HTTPException(status_code=404, detail="No tasks found")

    return todos
