from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from uuid import UUID
import uuid

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

class TaskR(AddTask):
    id: UUID = Field(default_factory=uuid.uuid4)
    