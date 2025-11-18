import asyncpg
from sqlalchemy.orm import declarative_base
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

DATABASE_URL = os.getenv("ASYNC_DB_URL")

engine = create_async_engine(DATABASE_URL, echo=True) 
AsyncSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
Base = declarative_base()
metadata = MetaData()


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

