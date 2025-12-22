from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from repository.users_repository import UsersRepository
from app.models.db_user import User
from sqlalchemy import select
from fastapi import HTTPException


class UsersService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repository = UsersRepository(db)

    async def register_user(self, email: str, password_hash: str) -> User:
        query = await self.db.execute(select(User).where(User.email == email))
        existing_user = query.scalars().first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        user = await self.repository.register_user(email, password_hash)
        return user
