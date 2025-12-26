
from fastapi import FastAPI
from app.endpoints import tasks, users


app = FastAPI(title="Todo API")
app.include_router(tasks.router)
app.include_router(users.router)


