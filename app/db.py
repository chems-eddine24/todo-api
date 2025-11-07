from sqlalchemy import Column, Integer, create_engine, text, MetaData, func, String
from sqlalchemy.orm import declarative_base, sessionmaker
import sqlalchemy as sa
import uuid
from sqlalchemy.dialects.postgresql import UUID as UUid
import os

engine = create_engine(os.getenv("DATABASE_URL"))
conn = engine.connect()
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
metadata = MetaData()


class Task(Base):
    __tablename__ = 'tasks'
    id = sa.Column(UUid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = sa.Column(sa.String, index=True)
    description = sa.Column(sa.String, index=True)
    status = sa.Column(sa.String, index=True)
    Date = sa.Column(sa.DateTime, server_default=func.now())
