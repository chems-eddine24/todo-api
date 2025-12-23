
from fastapi import HTTPException

class ErrorHandler:
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