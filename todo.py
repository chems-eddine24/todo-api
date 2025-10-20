from fastapi import FastAPI, HTTPException
from Projects.Models import *
from typing import Optional


todo = []

app = FastAPI(title="Todo API")


@app.get('/')
def home():
   return {"message":"Welcome to Todo API"}


@app.get('/todos/')
def get_all_tasks():
   return todo

@app.post("/todos/", response_model=Task)
def create_task(add_task: AddTask):
    task = Task(id=len(todo) + 1, **add_task.dict())
    todo.append(task)
    return task


@app.get('/todos/{task_id}/')
def get_task_by_id(task_id: int):
   for task in todo:
      if task.id == task_id:
         return task
   raise HTTPException(status_code=404, detail="Task not found!")

@app.patch('/todos/{task_id}/')
def edit_task(task_id: int, edit_task: EditTask):
   for task in todo:
    if task.id == task_id:
        task.title = edit_task.title
        task.description = edit_task.description
        task.status = edit_task.status
        task.Date = edit_task.Date
        return task
   raise HTTPException(status_code=404, detail="Task not found!")

@app.delete('/todos/{task_id}/')
def delete_task(task_id: int):
   for task in todo:
      if task.id == task_id:
         todo.remove(task)
         return {"message": "Task deleted successfully"}
   raise HTTPException(status_code=404, detail="Task not found!")

@app.get("/todos/search")
def get_todos_by_status_and_title(status: Optional[str] = None, title: Optional[str] = None):
    results = todo
    if status:
        results = [t for t in results if t.status.lower() == status.lower()]
    if title:
        results = [t for t in results if title.lower() in t.title.lower()]

    if not results:
        raise HTTPException(status_code=404, detail="No tasks found with the given filters")

    return results
