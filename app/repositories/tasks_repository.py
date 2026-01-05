from typing import List, Optional
from app.models.db_task import Task
from sqlalchemy.future import select
from app.repositories.base_repository import BaseRepository

class TasksRepository(BaseRepository):

    async def get_all_tasks(self, user_id: str) -> list[Task]:
        result = await self.session.execute(select(Task).where(Task.user_id == user_id))
        tasks = result.scalars().all()
        return tasks

    async def create_task(self, task: Task) -> Task:
        self.session.add(task)
        await self.session.commit()
        await self.session.refresh(task)
        return task
    
    async def get_task_by_id(self, task_id: str, user_id: str) -> Optional[Task]:
        result = await self.session.execute(select(Task).where(Task.id == task_id).where(Task.user_id == user_id))
        task = result.scalars().first()
        return task

   
    
    async def delete_task(self, task_id: str, user_id: str) -> bool:
        result = await self.session.execute(select(Task).where(Task.id == task_id).where(Task.user_id == user_id))
        task = result.scalars().first()
        if not task:
            return False
        await self.session.delete(task)
        await self.session.commit()
        return True
    
    async def get_tasks_by_status_and_title(self, user_id: str, status: Optional[str] = None, title: Optional[str] = None) -> List[Task]:
        query = select(Task).where(Task.user_id == user_id)

        if status:
            query = query.filter(Task.status == status).where(Task.user_id == user_id)

        if title:
            query = query.filter(Task.title == title).where(Task.user_id == user_id)

        result = await self.session.execute(query)
        tasks = result.scalars().all()
        return tasks
    
