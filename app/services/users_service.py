from app.core.exceptions import AppError, ErrorCode
from app.repositories.users_repository import UsersRepository
from fastapi import status, Response, Request, HTTPException
from app.models.db_user import User
from app.schemas.schemas_user import UserCreate
from app.services.base_service import BaseService
from app.core.security import (get_password_hash, verify_password, create_access_token, create_refresh_token, verify_access_token, verify_refresh_token)

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
    async def login_for_access_token(self, response: Response, email, password):
        user = await UsersService(self.session).login_user(email=email, password=password)
        if not user:
            raise AppError(
                message='User not found with the given email and password, passwrod or email incorrect',
                error_code=ErrorCode.USER_NOT_FOUND,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        user_id = user.id
        access_token = create_access_token(user_id=str(user_id))
        refresh_token = create_refresh_token(subject=str(user_id))
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
            value=refresh_token,
            httponly=True,
           samesite="lax",
           max_age=7*24*60*60,
           secure=False,
           path='/'
           )
        return {'message':f"welcome {user.email} "}
    
    async def refresh_access_token(self, response: Response, request: Request):
        refresh_token = request.cookies.get("refresh_token")
        if not refresh_token:
            raise HTTPException(
                status_code=401,
                detail="Refresh token missing",
                )
        payload = verify_refresh_token(refresh_token)
        user_id = payload.get("sub")
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
    

    async def logout(self, response: Response):
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        return {'message':'logged out'}
