from app.core.auth_config import get_password_hash
from app.core.error_handler import UserHandler
from app.schemas.schemas_user import UserR
from app.core.auth_config import *
from repository.users_repository import UsersRepository

class AuthService:

    def __init__(self, db):
        self.db = db


    async def authenticate_user(self, email: str, password: str) -> UserR :
        user = await UsersRepository(db=self.db).get_user_by_email(email)
        if not user or not verify_password(password, get_password_hash(password)):
            return UserHandler.wrong_email_or_password()
        return user

    