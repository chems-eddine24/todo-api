from sqlalchemy.orm import declarative_base
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.config import settings



engine = create_async_engine(settings.ASYNC_DATABASE_URL, echo=True) 
AsyncSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession ,expire_on_commit=False)
Base = declarative_base()
metadata = MetaData()


async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()   
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

