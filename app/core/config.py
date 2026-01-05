
from dotenv import load_dotenv
import os
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
load_dotenv()



class Settings:

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    ASYNC_DATABASE_URL = os.getenv("ASYNC_DB_URL")

settings = Settings()
