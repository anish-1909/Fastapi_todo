from fastapi import APIRouter
from ..models.todo import Todo
from ..services.todo_service import TodoService

router = APIRouter()

@router.get("/todos")
def get_todos():
    return TodoService.get_all_todos()

@router.post("/todos")
def create_todo(todo: Todo):
    return TodoService.add_todo(todo)

@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    return TodoService.delete_todo(todo_id)