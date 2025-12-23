from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from repository.users_repository import UsersRepository
from app.models.db_user import User
from sqlalchemy import select



class UsersService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repository = UsersRepository(db)

    async def register_user(self, email: str, password_hash: str) -> User:
        user = UsersRepository(db=self.db).register_user(email=email, password_hash=password_hash)
        return user
    
    async def login_user(self, user_id: str):
        user = UsersRepository(db=self.db).login_user(user_id=user_id)
        return user

