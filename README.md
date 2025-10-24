# Todo List API

A simple Todo List API built with **FastAPI**.  
It allows users to create, read, update, and delete tasks — all stored in memory (no database required).  
Perfect for learning CRUD operations and understanding FastAPI basics.

---

## Features :

• Create, read, update, and delete tasks  
• Search tasks by title or status  
• Manage tasks with unique IDs  
• Lightweight and beginner-friendly

---

## Tech Stack :

• Python 3.13  
• FastAPI  
• Pydantic  
• Uvicorn

---

## Setup & Run :

### Make sure you have **docker** installed, then run:
```
$ docker run -d -p 8000:8000 --name web chemseddine24/todo-app
```
#### this command will :

##### download the image chemseddine24/todo-app from docker hub
##### create a new container "web" 
##### start the fastapi app automatically

### The API will be available at:

http://127.0.0.1:8000

### Open the API docs:

Visit -> http://localhost:8000/docs

### API Endpoints :
• Method	Endpoint	Description :
```
GET	/Welcome message

GET	/todos/	Retrieve all tasks

GET	/todos/{task_id}/	Get task by ID

POST /todos/	Create a new task

PATCh /todos/{task_id}/	Update an existing task

DELETE /todos/{task_id}/	Delete a task

GET	/todos/search	 Search tasks by status or title
```
### Project Structure :

todo_api/
```
|── .dockerignore
├── .gitignore
├── Pipfile
├── Pipfile.lock
├── README.md
├── Dockerfile
├── todo.py          
├── schemas.py       
└── __pycache__/    
```
    
### Author :
https://github.com/chems-eddine24
