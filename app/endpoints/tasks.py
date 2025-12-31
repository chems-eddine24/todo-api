from fastapi import APIRouter, Depends
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db_core import get_db
from app.schemas.schemas_task import TaskR, AddTask, EditTask
from app.models.db_user import User
from app.core.auth_config import get_current_user
from service.tasks_service import TaskService

router = APIRouter(prefix="/todos", tags=["todos"])

@router.get("/", response_model=list[TaskR])
async def get_all_tasks(current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    tasks = await TaskService(db).get_all_tasks(current_user.id)
    return tasks


@router.post("/", response_model=TaskR)
async def create_task(add_task: AddTask, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    task = await TaskService(db).create_task(current_user.id, add_task)
    return task


@router.get("/{task_id}/", response_model=TaskR)
async def get_task_by_id(task_id, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await TaskService(db).get_task_by_id(task_id, current_user.id)
    

@router.patch("/{task_id}/", response_model=TaskR)
async def edit_task(task_id: str, edit_task: EditTask, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await TaskService(db).edit_task(task_id, edit_task, current_user.id)

@router.delete("/{task_id}/")
async def delete_task(task_id: str, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await TaskService(db).delete_task(task_id, current_user.id)
        


@router.get("/search", response_model=list[TaskR])
async def get_todos_by_status_and_title(status: Optional[str] = None, title: Optional[str] = None, current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    tasks = await TaskService(db).get_tasks_by_status_and_title(current_user.id, status, title)
    return tasks
