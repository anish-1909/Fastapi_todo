from ..storage.data import todos

class TodoService:

    @staticmethod
    def get_all_todos():
        return todos

    @staticmethod
    def add_todo(todo):
        todos.append(todo)
        return todo
    @staticmethod
    def delete_todo(todo_id):

        for todo in todos:

            if todo.id == todo_id:
                todos.remove(todo)

                return {
                    "message": "Todo deleted successfully"
                }

        return {
            "message": "Todo not found"
        }