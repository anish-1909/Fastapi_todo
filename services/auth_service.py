from ..storage.data import users

class AuthService:

    @staticmethod
    def register(username, password):
        if username in users:
            return {"message": "User already exists"}
        
        users[username] = password
        return {"message": "Registration Successful"}

    @staticmethod
    def login(username, password):

        if username in users and users[username] == password:
            return {"message": "Login Successful"}

        return {"message": "Invalid Credentials"}