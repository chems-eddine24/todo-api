
from fastapi import HTTPException

class TaskHandler:
    @staticmethod
    def handle_user_not_found():
        raise HTTPException(status_code=404, detail="User not found")

    @staticmethod
    def handle_task_not_found():
        raise HTTPException(status_code=404, detail="Task not found")
    
    @staticmethod
    def handle_no_title_provided():
        raise HTTPException(status_code=400, detail="Task should have a valid title!")
    
    @staticmethod
    def handle_status_title_filter_missing():
        raise HTTPException(status_code=400, detail="At least one filter (status or title) must be provided")
    
    @staticmethod
    def handle_no_tasks_with_criteria():
        raise HTTPException(status_code=404, detail="No tasks found with the given criteria")
    
class UserHandler:

    @staticmethod
    def wrong_email_or_password():
        raise HTTPException(status_code=400, detail="Wrong Email or Password!")
    
    @staticmethod
    def refrsh_token_error():
        raise HTTPException(status_code=401, detail="Refresh Token Missing!")
    
    @staticmethod
    def user_not_found():
        raise HTTPException(status_code=404, detail="User Not Found")
    
    @staticmethod
    def existing_user_error():
        raise HTTPException(status_code=404, detail="Existing User With This Email!")
    
    @staticmethod
    def email_error():
        raise HTTPException(status_code=404, detail="Email Required!")
    
    