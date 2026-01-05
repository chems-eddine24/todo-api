from app.core.error_handler import UserHandler
from app.repositories.users_repository import UsersRepository
from app.models.db_user import User
from app.schemas.schemas_user import UserCreate
from app.core.security import authenticate_user
from app.services.base_service import BaseService
from app.core.security import get_password_hash, verify_password

class UsersService(BaseService):
    def __init__(self, session):
        super().__init__(session)
        self.user_repo = UsersRepository(session)

    async def register_user(self, data: UserCreate):
        user = User(
            email=data.email,
            password_hash=get_password_hash(data.password)
            )
        if await self.user_repo.get_user_by_email(user.email):
            return UserHandler.existing_user_error()
        if user.email is None or user.email == "":
            return UserHandler.email_error()
        user = await self.user_repo.register_user(user=user)
        return user
    
    async def login_user(self, email: str, password: str):
        user = await self.user_repo.get_user_by_email(email)
        if not user or not verify_password(password, get_password_hash(password)):
            return False
        return user