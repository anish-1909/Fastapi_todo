from fastapi import FastAPI

from .api.auth import router as auth_router
from .api.todo import router as todo_router

app = FastAPI(
    title="Todo App"
)

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    todo_router,
    tags=["Todos"]
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Todo App"
    }