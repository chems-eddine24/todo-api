from enum import Enum


class ErrorCode(Enum):
    USER_NOT_FOUND = " User Does Not Exist"
    TASK_NOT_FOUND = " No Task Found"
    INVALID_TASK_TITLE = "Task Should Have A Valid Title"
    INVALID_TASK_ID = "Wrong Task ID"
    MISSING_FILTER = "At Least One Filter (Status Or Title) Most Be Provided"
    TASK_CRITERIA_INVALID = "No Task Found With The Given Criteria"
    WRONG_EMAIL_OR_PASSWORD = "Wrong Email Or Password"
    RFRESH_TOKEN_ERROR = "Refresh Token Is Missing"
    USER_ALREADY_EXISTS = "Existing User With This Email"
    NO_EMAIL_PROVIDED = "Email Required"
    UNKWON_ERROR = "Unkwon Error"
    

class AppError(Exception):
    def __init__(self, message: str, error_code: ErrorCode = ErrorCode.UNKWON_ERROR, status_code: int = 500):
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.status_code = status_code
        