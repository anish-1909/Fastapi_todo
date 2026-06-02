# FastAPI Todo Application

A simple Todo Management REST API built using FastAPI and Pydantic. The project follows a layered architecture with separate modules for API routes, business logic, data models, and storage.

## Features

* Create Todo
* View All Todos
* View Todo by ID
* Delete Todo
* User Authentication
* Request Validation using Pydantic
* Interactive Swagger Documentation
* Modular Project Structure

---

## Project Structure

```text
Fastapi_todo/
│
├── api/
│   ├── auth.py
│   └── todo.py
│
├── core/
│   ├── config.py
│   └── exceptions.py
│
├── models/
│   ├── todo.py
│   └── user.py
│
├── services/
│   ├── auth_service.py
│   └── todo_service.py
│
├── storage/
│   └── data.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Technologies Used

* Python 3.x
* FastAPI
* Pydantic
* Uvicorn
* REST API

---

## Installation

### Clone Repository

```bash
git clone https://github.com/anish-1909/Fastapi_todo.git
cd Fastapi_todo
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```



### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
uvicorn Fastapi_todo.main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## Available Endpoints

### Authentication

| Method | Endpoint       | Description   |
| ------ | -------------- | ------------- |
| POST   | /auth/register | Register User |
| POST   | /auth/login    | Login User    |

### Todos

| Method | Endpoint    | Description    |
| ------ | ----------- | -------------- |
| GET    | /todos      | Get All Todos  |
| POST   | /todos      | Create Todo    |
| DELETE | /todos/{id} | Delete Todo    |

---

## Sample Todo Request

```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "completed": false
}
```

---

## Learning Outcomes

This project demonstrates:

* REST API Development
* FastAPI Framework
* Pydantic Validation
* API Routing
* Layered Architecture
* CRUD Operations
* Request and Response Handling


---

## Author

Anish A S
