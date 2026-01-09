from app.services.tasks_service import TaskService
from app.services.users_service import UsersService
from app.core.db_core import get_db
from fastapi import Depends

async def get_user_service(session = Depends(get_db)):
    return UsersService(session=session)

async def get_task_service(session = Depends(get_db)):
    return TaskService(session=session)
