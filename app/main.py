from fastapi import FastAPI
from app.endpoints import auth, tasks

app = FastAPI(title="Todo API")
app.include_router(tasks.router)
app.include_router(auth.router)


