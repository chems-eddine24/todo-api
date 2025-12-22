from app.core.db_core import *
from sqlalchemy import func
import sqlalchemy as sa
import uuid
from sqlalchemy.dialects.postgresql import UUID as UUid
from sqlalchemy.orm import relationship
from sqlalchemy import DateTime

class Task(Base):
    __tablename__ = 'tasks'
    id = sa.Column(UUid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = sa.Column(sa.String, index=True)
    description = sa.Column(sa.String, index=True)
    status = sa.Column(sa.String, index=True)
    date = sa.Column(DateTime(timezone=True), nullable=False)
    user_id = sa.Column(UUid(as_uuid=True), sa.ForeignKey('users.id'))
    user = relationship("User", back_populates="tasks")