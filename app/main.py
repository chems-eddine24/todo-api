
from fastapi import FastAPI, HTTPException, Depends, APIRouter, status
from requests import Session
from app.schemas.schemas_task import *
from app.schemas.schemas_user import *
from typing import Optional
from app.models.db_task import *
from app.core.db_core import *
from app.models.db_user import *
from app.models.db_task import *
from app.endpoints import tasks, users
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.endpoints.auth import get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from repository.tasks_repository import TasksRepository

app = FastAPI(title="Todo API")
app.include_router(tasks.router)
app.include_router(users.router)


