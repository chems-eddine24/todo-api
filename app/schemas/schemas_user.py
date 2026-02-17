from pydantic import BaseModel, ConfigDict
from uuid import UUID


class UserCreate(BaseModel):
    email: str
    password: str

class UserR(BaseModel):
    id: UUID 
    email: str
    class ConfigDict:
        model_config = ConfigDict(from_attributes=True)
        
class Token(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str
