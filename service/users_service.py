from app.core.error_handler import UserHandler
from repository.users_repository import UsersRepository
from app.schemas.schemas_user import UserR
from service.auth_service import AuthService


class UsersService:
    def __init__(self, db):
        self.db = db

    async def register_user(self, email: str, password_hash: str) -> UserR:
        if await UsersRepository(self.db).get_user_by_email(email):
            return UserHandler.existing_user_error()
        if email is None or email == "":
            return UserHandler.email_error()
        user = await UsersRepository(db=self.db).register_user(email=email, password_hash=password_hash)
        return user
    
    async def login_user(self, email: str, password: str):
        user = await AuthService(db=self.db).authenticate_user(email, password)
        return user



