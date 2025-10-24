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

### Clone the repository:
```bash
$ git clone https://github.com/chems-eddine24/todo_api.git
  ```
### Navigate to the project directory:
```bash
$ cd todo_api
```
### Build the docker image:
```
$ docker build -t todo-app .
```

### Run the container:
```
$ docker run -d -p 8000:8000 todo-app
```
The API will be available at:

http://127.0.0.1:8000

Open the API docs:

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
