from repository.tasks_repository import TasksRepository
from fastapi import  HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from app.schemas.schemas_task import AddTask, TaskR, EditTask
from app.models.db_task import Task
import uuid

class TaskService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.tasks_repository = TasksRepository(db)

    async def get_all_tasks(self, user_id: str) -> list[TaskR]:
        tasks = await self.tasks_repository.get_all_tasks(user_id)
        if not tasks:
            raise HTTPException(status_code=404, detail="No tasks found!")
        return tasks

    async def create_task(self, user_id: str, task_data: AddTask) -> TaskR:
        if task_data.title is None or task_data.title == "":
            raise HTTPException(status_code=400, detail="Task should have a valide title!")
        
        task = Task(
            title=task_data.title,
            description=task_data.description,
            status=task_data.status,
            date=task_data.date,
            user_id=user_id
        )
        return await self.tasks_repository.create_task(task)
    
    async def edit_task(self, task_id: str, edit_task_data: EditTask, user_id: str) -> Optional[TaskR]:
        task = await self.tasks_repository.get_task_by_id(task_id, user_id)
        if not task:
           raise HTTPException(404, "Task not found")
        
        task.title = edit_task_data.title if edit_task_data.title is not None else task.title
        task.description = edit_task_data.description if edit_task_data.description is not None else task.description
        task.status = edit_task_data.status if edit_task_data.status is not None else task.status
        task.date = edit_task_data.date if edit_task_data.date is not None else task.date

        await self.db.commit()
        await self.db.refresh(task)
        return task

    async def get_task_by_id(self, task_id, user_id: str) -> Optional[TaskR]:
        task = await self.tasks_repository.get_task_by_id(task_id, user_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task

    async def delete_task(self, task_id, user_id: str) -> bool:
        if type(task_id) != type(uuid.uuid4()):
            raise HTTPException(status_code=400, detail="Invalid task ID format")
        deleted_task = await self.tasks_repository.delete_task(task_id, user_id)
        if not deleted_task:
            raise HTTPException(status_code=404, detail="Task not found")
        return True

    async def get_tasks_by_status_and_title(self, user_id: str, status: Optional[str] = None, title: Optional[str] = None) -> Optional[TaskR]:
        if not status and not title:
            raise HTTPException(status_code=400, detail="At least one filter (status or title) must be provided")
        
        tasks = await self.tasks_repository.get_tasks_by_status_and_title(user_id, status, title)
        if not tasks:
            raise HTTPException(status_code=404, detail="No tasks found with the given criteria")
        return tasks
        

   