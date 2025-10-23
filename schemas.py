from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from uuid import uuid4

class AddTask(BaseModel):
    title: str
    description: str
    status: str
    Date: Optional[date] = None

class EditTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    Date: Optional[date] = None

class Task(AddTask):
    id: str = Field(default_factory=lambda: str(uuid4()))
    