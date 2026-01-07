from fastapi import APIRouter, Depends, Response, Request
from app.models.db_user import User
from app.schemas.schemas_user import UserCreate, UserR
from fastapi.security import OAuth2PasswordRequestForm
from app.dependencies.factories import *
from app.core.security import get_current_user
from app.services.auth_service import AuthService
from app.services.users_service import UsersService


router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post('/register', response_model=UserR)
async def register_user(user: UserCreate, user_service: UsersService = Depends(get_user_service)):
    return await user_service.register_user(user)

@router.post('/login')
async def login_for_access_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends(), auth_service: AuthService = Depends(get_auth_service)):
    return await auth_service.login_for_access_token(response, form_data.username, form_data.password)

@router.post('/refresh')
async def refresh_access_token(response: Response, request: Request, auth_service: AuthService = Depends(get_auth_service)):
    return await auth_service.refresh_access_token(response, request)

@router.get('/me', response_model=UserR)
async def about_current_user(current_user: User = Depends(get_current_user)):
    return current_user

@router.delete('/logout')
async def logout_user(response: Response, auth_service: AuthService = Depends(get_auth_service)):
    return await auth_service.logout(response)