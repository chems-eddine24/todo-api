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

• git clone https://github.com/chems-eddine24/todo_api.git
  
### Navigate to the project directory:
• cd todo_api

### Install dependencies:
• pip install fastapi uvicorn

### Run the application:
• uvicorn main:app --reload


### API Endpoints :
• Method	Endpoint	Description :

##### GET	/	Welcome message

##### GET	/todos/	Retrieve all tasks

##### GET	/todos/{task_id}/	Get task by ID

##### POST	/todos/	Create a new task

##### PATCH	/todos/{task_id}/	Update an existing task

##### DELETE	/todos/{task_id}/	Delete a task

##### GET	/todos/search	Search tasks by status or title

### Project Structure :

todo_api/

    ├── main.py
    
    ├── models.py
    
    └── README.md
    
### Author :
https://github.com/chems-eddine24
