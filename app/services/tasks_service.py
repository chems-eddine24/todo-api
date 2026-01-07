from app.repositories.tasks_repository import TasksRepository
from app.services.base_service import BaseService
from typing import Optional
from app.schemas.schemas_task import AddTask, TaskR, EditTask
from app.models.db_task import Task
from app.core.exceptions import AppError, ErrorCode
from fastapi import status as status_code

class TaskService(BaseService):
    def __init__(self, session):
        super().__init__(session)
        self.task_repo = TasksRepository(session=session)

    async def get_all_tasks(self, user_id: str) -> list[TaskR]:
        tasks = await self.task_repo.get_all_tasks(user_id)
        if not tasks:
            raise AppError(
                message='no task found, make sure you have added some tasks first',
                error_code=ErrorCode.TASK_NOT_FOUND,
                status_code=status_code.HTTP_400_BAD_REQUEST
            )
        return tasks

    async def create_task(self, user_id: str, task_data: AddTask) -> TaskR:
        
        if task_data.title is None or task_data.title == "":
            raise AppError(
                message="A task most have a title (field required)",
                error_code=ErrorCode.INVALID_TASK_TITLE,
                status_code=status_code.HTTP_403_FORBIDDEN
            )
        task = Task(
            title=task_data.title,
            description=task_data.description,
            status=task_data.status,
            date=task_data.date,
            user_id=user_id
        )
        return await self.task_repo.create_task(task)
    
    async def edit_task(self, task_id: str, edit_task_data: EditTask, user_id: str) -> Optional[TaskR]:
        try:
            task = await self.task_repo.get_task_by_id(task_id, user_id)
            task.title = edit_task_data.title if edit_task_data.title != "" else task.title
            task.date = edit_task_data.date if edit_task_data.date != "" else task.date
            task.description = edit_task_data.description if edit_task_data.description != "" else task.description
            task.status = edit_task_data.status if edit_task_data.status != "" else task.status
            return task
        except Exception:
            raise AppError(
                message='ID given is incorrect',
                error_code=ErrorCode.TASK_NOT_FOUND,
                status_code=status_code.HTTP_400_BAD_REQUEST
            )
    async def get_task_by_id(self, task_id, user_id: str) -> Optional[TaskR]:
        try:
            return await self.task_repo.get_task_by_id(task_id, user_id)
        except Exception as e:
            raise AppError(
                message='ID given is incorrect',
                error_code=ErrorCode.INVALID_TASK_ID,
                status_code=status_code.HTTP_400_BAD_REQUEST
            )

    async def delete_task(self, task_id, user_id: str) -> dict:
        try:
            task_to_delete = await self.task_repo.delete_task(task_id, user_id)
            if task_to_delete:
                return {'message': 'Task deleted successfully'} 
        except Exception as e:
            raise AppError(
                message='the ID given is incorrect',
                error_code=ErrorCode.INVALID_TASK_ID,
                status_code=status_code.HTTP_400_BAD_REQUEST
            )

    async def get_tasks_by_status_and_title(self, user_id: str, status: Optional[str] = None, title: Optional[str] = None) -> Optional[TaskR]:
        if not status and not title:
            raise AppError(
                message='status and title field are empty, provid valide title or status to get the task wanted',
                error_code=ErrorCode.MISSING_FILTER,
                status_code=status_code.HTTP_400_BAD_REQUEST
            )
        
        tasks = await self.task_repo.get_tasks_by_status_and_title(user_id, status, title)
        if not tasks:
            raise AppError(
                message="enter valide task's status or title to get your task",
                error_code=ErrorCode.TASK_CRITERIA_INVALID,
                status_code=status_code.HTTP_404_NOT_FOUND
            )
        return tasks
        

