from fastapi import APIRouter, HTTPException, Depends, Response
from sqlalchemy import select
from app.core.db_core import AsyncSessionLocal, get_db
from app.models.db_user import User
from app.schemas.schemas_user import UserCreate, UserR
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm
from app.endpoints.auth import *
from service.users_service import UsersService



router = APIRouter(prefix="/users", tags=["users"])

@router.post('/register', response_model=UserR)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    user = await UsersService(db).register_user(email=user.email, password_hash=get_password_hash(user.password))
    return user

@router.post('/login')
async def login_for_access_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Incorrect email or password"
        )
    access_token = create_access_token(user_id=str(user.id))
    refresh = create_refresh_token(subject=str(user.id)) 
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        samesite="lax",
        max_age=1800,
        secure=False,
        path='/'
    )
    response.set_cookie(
        key="refresh_token",
        value=refresh,
        httponly=True,
        samesite="lax",
        max_age=7*24*60*60,
        secure=False,
        path='/'
    )
    return {'message':f'welcome {user.email}'}

@router.post('/refresh')
async def refresh_access_token(response: Response, request: Request, db: AsyncSession = Depends(get_db)):
    refresh_token = request.cookies.get("refresh_token")
    if not refresh_token:
        raise HTTPException(
            status_code=401,
            detail="Refresh token missing",
        )
    payload = verify_refresh_token(refresh_token)
    user_id = payload.get("sub")
    user = await UsersService(db).login_user(user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )
    new_access_token = create_access_token(user_id=user_id)
    new_refresh_token = create_refresh_token(subject=user_id)
    response.set_cookie(
        key="access_token",
        value=new_access_token,
        httponly=True,
        samesite="lax",
        max_age=1800,
        secure=False,
        path='/'
    )
    response.set_cookie(
        key="refresh_token",
        value=new_refresh_token,
        httponly=True,
        samesite="lax",
        max_age=7*24*60*60,
        secure=False,
        path='/'
    )
    return {'message': 'access token refreshed successfully'}

@router.get('/me', response_model=UserR)
async def about_current_user(current_user: User = Depends(get_current_user)):
    return current_user

@router.delete('/logout')
async def logout_user(response: Response):
    response.delete_cookie(key="access_token")
    response.delete_cookie(key="refresh_token")
    return {"message": "Logged out"}