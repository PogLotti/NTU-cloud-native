# user_controller.py

class UserController:
    def __init__(self, service):
        self.service = service

    def register(self, username: str):
        return self.service.register_user(username)