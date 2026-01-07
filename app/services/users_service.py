from app.core.exceptions import AppError, ErrorCode
from app.repositories.users_repository import UsersRepository
from fastapi import status
from app.models.db_user import User
from app.schemas.schemas_user import UserCreate
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
            raise AppError(
                message='the email address given is already used by an another account',
                error_code=ErrorCode.USER_ALREADY_EXISTS,
                status_code=status.HTTP_403_FORBIDDEN
            )
        if user.email is None or user.email == "":
            raise AppError(
                message='you must enter an email to register',
                error_code=ErrorCode.NO_EMAIL_PROVIDED,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        user = await self.user_repo.register_user(user=user)
        return user
    
    async def login_user(self, email: str, password: str):
        user = await self.user_repo.get_user_by_email(email)
        if not user or not verify_password(password, get_password_hash(password)):
            return False
        return user