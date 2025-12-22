from sqlalchemy import Column, String, Integer
from app.core.db_core import *
from sqlalchemy.dialects.postgresql import UUID as UUid
import uuid
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(UUid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)

    tasks = relationship("Task", back_populates="user")
