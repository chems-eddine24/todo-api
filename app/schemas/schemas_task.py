from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
import uuid
from datetime import datetime

class AddTask(BaseModel):
    title: str
    description: str
    status: str
    date: datetime

class EditTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    date: Optional[datetime] = None

class TaskR(AddTask):
    id: UUID = Field(default_factory=uuid.uuid4)

    model_config = {
        "from_attributes": True
    }


    