from sqlalchemy.future import select
from app.models.db_user import User
from app.schemas.schemas_user import UserR
from app.repositories.base_repository import BaseRepository
from app.schemas.schemas_user import UserCreate



class UsersRepository(BaseRepository):

    async def register_user(self, user: User) -> UserR:
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
    
    async def get_user_by_email(self, email: str) -> UserR :
       user = await self.session.execute(select(User).where(User.email == email))
       return user.scalars().first()
    
    async def get_user_by_id(self, id: str):
        user = await self.session.execute(select(User).where(User.id == id))
        return user.scalars().first()
    
