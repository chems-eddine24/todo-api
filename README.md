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
### Install dependencies with Pipenv:
Make sure you have Pipenv installed. If not:
```
$ pip install pipenv
```
Then install all dependencies:
```
pipenv install
```
This will automatically create a virtual environment and install everything from the Pipfile.lock

Activate the virtual environment:
```
pipenv shell
```

### Run the application:
```
$ uvicorn main:app --reload
```
The API will be available at:

http://127.0.0.1:8000

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
│
├── .gitignore
├── Pipfile
├── Pipfile.lock
├── README.md
│
├── todo.py          # Main FastAPI app (entry point)
├── schemas.py       # Pydantic models / data validation
│
└── __pycache__/     # (ignored by Git)
```
    
### Author :
https://github.com/chems-eddine24
