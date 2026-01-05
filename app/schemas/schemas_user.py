from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID
import uuid

class UserCreate(BaseModel):
    email: str
    password: str

class UserR(BaseModel):
    id: UUID 
    email: str

    class Config:
        model_config = ConfigDict(from_attributes=True)
        
class Token(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str
