from app.repositories.tasks_repository import TasksRepository
from app.services.base_service import BaseService
from typing import Optional
from app.schemas.schemas_task import AddTask, TaskR, EditTask
from app.models.db_task import Task
from app.core.error_handler import TaskHandler

class TaskService(BaseService):

    def __init__(self, session):
        super().__init__(session)
        self.task_repo = TasksRepository(session)

    async def get_all_tasks(self, user_id: str) -> list[TaskR]:
        tasks = await self.task_repo.get_all_tasks(user_id)
        if not tasks:
            return TaskHandler.handle_task_not_found()
        return tasks

    async def create_task(self, user_id: str, task_data: AddTask) -> TaskR:
        if task_data.title is None or task_data.title == "":
            return TaskHandler.handle_no_title_provided()        
        task = Task(
            title=task_data.title,
            description=task_data.description,
            status=task_data.status,
            date=task_data.date,
            user_id=user_id
        )
        return await self.task_repo.create_task(task)
    
    async def edit_task(self, task_id: str, edit_task_data: EditTask, user_id: str) -> Optional[TaskR]:
        task = await TasksRepository().get_task_by_id(task_id, user_id)
        if not task:
            return TaskHandler.handle_task_not_found()
        task.title = edit_task_data.title if edit_task_data.title != "" else task.title
        task.date = edit_task_data.date if edit_task_data.date != "" else task.date
        task.description = edit_task_data.description if edit_task_data.description != "" else task.description
        task.status = edit_task_data.status if edit_task_data.status != "" else task.status
        self.session.commit()
        self.session.refresh(task)
        
        return task

    async def get_task_by_id(self, task_id, user_id: str) -> Optional[TaskR]:
        try:
            return await self.task_repo.get_task_by_id(task_id, user_id)
        except Exception as e:
            return TaskHandler.handle_task_not_found()

    async def delete_task(self, task_id, user_id: str) -> dict:
        try:
            task_to_delete = await self.task_repo.delete_task(task_id, user_id)
            return {'message': 'Task deleted successfully'} if task_to_delete else TaskHandler.handle_task_not_found()
        except Exception as e:
            return TaskHandler.handle_task_not_found()

    async def get_tasks_by_status_and_title(self, user_id: str, status: Optional[str] = None, title: Optional[str] = None) -> Optional[TaskR]:
        if not status and not title:
            return TaskHandler.handle_status_title_filter_missing()
        
        tasks = await self.task_repo.get_tasks_by_status_and_title(user_id, status, title)
        if not tasks:
            return TaskHandler.handle_no_tasks_with_criteria()
        return tasks
        

