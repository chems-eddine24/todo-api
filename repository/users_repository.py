from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.db_user import User
from app.schemas.schemas_user import UserR



class UsersRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def register_user(self, email: str, password_hash: str) -> UserR:
        user = User(
            email=email,
            password_hash=password_hash
        )
        
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user
    
    async def get_user_by_email(self, email: str) -> UserR :
        user = await self.db.execute(select(User).where(User.email == email))
        return user.scalars().first()
    
    async def get_user_by_id(self, id: str):
        user = await self.db.execute(select(User).where(User.id == id))
        return user.scalars().first()

