from fastapi import Depends, Response
from app.services.base_service import BaseService
from app.core.security import *
from app.services.users_service import UsersService


class AuthService(BaseService):

    async def login_for_access_token(self, response: Response, email, password):
        user = await UsersService(self.session).login_user(email=email, password=password)
        access_token = create_access_token(user_id=str(user.id))
        refresh_token = create_refresh_token(subject=str(user.id))
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

