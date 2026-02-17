import pytest
import httpx
import os
from sqlalchemy import delete
from app.main import app
from app.models.db_user import User
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.db_core import get_db, Base
from sqlalchemy.pool import NullPool
from dotenv import load_dotenv
load_dotenv()


engine = create_async_engine(os.getenv("ASYNC_TEST_DB"), pool_pre_ping=True, poolclass=NullPool)
sessionlocal = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
async def override_get_db():
   async with sessionlocal() as s:
      yield s
      await s.rollback()
app.dependency_overrides[get_db] = override_get_db



test_user = {"email":"test@gmail.com", "password":"test123"}
async def create_user(client: httpx.AsyncClient, user_data: dict):
   res = await client.post("/api/auth/register", json=user_data)
   assert res.status_code == 200
   return res.json()

async def delete_user():
   async with sessionlocal() as session:
      await session.execute(delete(User).where(User.email == test_user['email']))
      await session.commit()
   

   


@pytest.fixture
async def client():
   async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://test") as c:
      yield c

@pytest.fixture
async def login(client):
   await create_user(client, test_user)
   login_info = {"username":test_user['email'], "password":test_user['password']}
   res = await client.post("/api/auth/login", data=login_info)
   assert res.status_code == 200
   yield res
   await delete_user()

   