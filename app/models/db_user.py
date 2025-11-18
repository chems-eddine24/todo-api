from sqlalchemy import Column, String, Integer
from app.db.core import *
from sqlalchemy.dialects.postgresql import UUID as UUid
import uuid


class User(Base):
    __tablename__ = 'users'
    id = Column(UUid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
