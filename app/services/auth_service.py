from fastapi import Response
from app.services.base_service import BaseService
from app.core.security import *
from app.services.users_service import UsersService


class AuthService(BaseService):
    def __init__(self, session):
        super().__init__(session)
        self.user_service = UsersService(session)

    async def login_for_access_token(self, response: Response, email, password):
        user = await self.user_service.login_user(email=email, password=password)
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

