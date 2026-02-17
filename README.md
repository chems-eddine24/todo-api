# Todo List API

A production-ready Todo REST API built with FastAPI featuring JWT authentication, HTTP-only cookies, and full endpoint testing with Pytest.

---

## Features :

• User registration & login

• JWT authentication (Access + Refresh tokens)

• HTTP-only cookie-based auth

• Create, update, delete, and list tasks

• Protected routes

• Async endpoints

• Docker 

• Pytest test suite

• Clean architecture

---

## Tech Stack :

• Framework: FastAPI  

• Database: PostgreSQL

• ORM: SQLAlchemy

• Authentication: JWT

• Testing: Pytest

• Containerization: Docker & Docker Compose


---

## Setup & Run :

### Clone the repository:
```
$ git clone https://github.com/chemseddine24/todo-api.git

$ cd todo-api
```
## run migrations inside the docker container:
```
$ alembic upgrade head
```

## Make sure you have docker installed, then build and run the container with:
```
$ docker compose up
```

### The API will be available at:

http://127.0.0.1:8000

### Open the API docs:

Visit -> http://localhost:8000/docs


### Project Structure :

todo_api/
```
todo-api/
├── app/
    ├── core/
    └── dependecies/
    └── endpoints/
    └── models/
    └── repositories/
    └── schemas/
    └── services/
└── migrations/
└── tests/
├── Dockerfile           
├── docker-compose.yml
└── pyproject.toml 
├── Pipfile / Pipfile.lock 
└── README.md
```
    
### Author :
https://github.com/chems-eddine24
