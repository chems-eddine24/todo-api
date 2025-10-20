from pydantic import BaseModel
from typing import Optional
from datetime import date

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
    id: int