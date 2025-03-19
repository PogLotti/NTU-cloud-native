# user_repo.py

class UserRepository:
    def __init__(self):
        # Store users with lower-cased keys to enforce case insensitivity.
        self.users = {}

    def add_user(self, username):
        key = username.lower()
        if key in self.users:
            return False
        self.users[key] = username
        return True

    def exists(self, username):
        return username.lower() in self.users