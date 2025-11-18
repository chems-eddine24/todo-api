from app.db.core import *
from app.models.db_user import *
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.schemas_user import *




def get_password_hash(password: str) -> str:
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()


async def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()

async def get_user_by_id(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

async def create_user(add_user: UserCreate, db: Session = Depends(get_db)):
    user = User(
        email=add_user.email,
        password_hash=get_password_hash(add_user.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

async def delete_user(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
