from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from app.db.core import AsyncSessionLocal, get_db
from app.models.db_user import User
from app.schemas.schemas_user import UserCreate, UserR, Token
from sqlalchemy.ext.asyncio import AsyncSession
import random
from passlib.context import CryptContext


#Security utilities
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

router = APIRouter(prefix="/users", tags=["users"])

@router.post('/', response_model=UserR)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    query = await db.execute(select(User).filter(User.email == user.email))
    existing_user = query.scalars().first()
    if existing_user:
        raise HTTPException(
            detail="User with this email already exists",
            status_code=400
        )
    user = User(
        email=user.email,
        password_hash=get_password_hash(user.password)
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

@router.post('/', response_model=Token)
async def login_for_access_token(user: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).filter(User.email == user.email))
    db_user = result.scalars().first()
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
        )

    token = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=50))
    return {"access_token": token, "token_type": "bearer"}