from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
import uuid

class UserCreate(BaseModel):
    email: str
    password: str

class UserR(BaseModel):
    id: UUID = Field(default_factory=uuid.uuid4)
    email: str

    class Config:
        from_attributes = True
        
class Token(BaseModel):
    access_token: str
    token_type: str
