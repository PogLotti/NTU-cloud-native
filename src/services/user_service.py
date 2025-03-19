# user_service.py

class UserService:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def register_user(self, username):
        if self.user_repo.exists(username):
            return "Error - user already existing"
        self.user_repo.add_user(username)
        return "Success"
    
    def user_exists(self, username):
        return self.user_repo.exists(username)