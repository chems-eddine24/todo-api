from typing import  Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.db_user import User



class UsersRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def register_user(self, email: str, password_hash: str) -> User:
        query = await self.db.execute(select(User).where(User.email == email))
        user = User(
            email=email,
            password_hash=password_hash
        )
        
        self.db.add(user)
        return user
    
    async def login_user(self, user_id: str):
        user = await self.db.execute(select(User).where(User.id == user_id))
        return user

