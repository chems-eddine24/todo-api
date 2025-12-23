from repository.tasks_repository import TasksRepository
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from app.schemas.schemas_task import AddTask, TaskR, EditTask
from app.models.db_task import Task
from app.core.error_handler import ErrorHandler

class TaskService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.tasks_repository = TasksRepository(db)

    async def get_all_tasks(self, user_id: str) -> list[TaskR]:
        tasks = await self.tasks_repository.get_all_tasks(user_id)
        if not tasks:
            return ErrorHandler.handle_task_not_found()
        return tasks

    async def create_task(self, user_id: str, task_data: AddTask) -> TaskR:
        if task_data.title is None or task_data.title == "":
            return ErrorHandler.handle_no_title_provided()        
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
            return ErrorHandler.handle_task_not_found()
        
        task.title = edit_task_data.title if edit_task_data.title is not None else task.title
        task.description = edit_task_data.description if edit_task_data.description is not None else task.description
        task.status = edit_task_data.status if edit_task_data.status is not None else task.status
        task.date = edit_task_data.date if edit_task_data.date is not None else task.date

        
        return task

    async def get_task_by_id(self, task_id, user_id: str) -> Optional[TaskR]:
        try:
            return await self.tasks_repository.get_task_by_id(task_id, user_id)
        except Exception as e:
            return ErrorHandler.handle_task_not_found()

    async def delete_task(self, task_id, user_id: str) -> dict:
        try:
            task_to_delete = await self.tasks_repository.delete_task(task_id, user_id)
            return {'message': 'Task deleted successfully'} if task_to_delete else ErrorHandler.handle_task_not_found()
        except Exception as e:
            return ErrorHandler.handle_task_not_found()

    async def get_tasks_by_status_and_title(self, user_id: str, status: Optional[str] = None, title: Optional[str] = None) -> Optional[TaskR]:
        if not status and not title:
            return ErrorHandler.handle_status_title_filter_missing()
        
        tasks = await self.tasks_repository.get_tasks_by_status_and_title(user_id, status, title)
        if not tasks:
            return ErrorHandler.handle_no_tasks_with_criteria()
        return tasks
        

   