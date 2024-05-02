import bcrypt
import rich
from rich.panel import Panel
import inquirer

class user:

    def __init__(self, username, password, id, decode=False):
        self.id = id
        self.username = username
        if decode:
            self.password = password
        else:
            self.password = self.hash_password(password)
        self.wins = 0

    def get_username(self):
        return self.username

    def get_wins(self):
        return self.wins

    def hash_password(self, password):
        # Hash the password using bcrypt
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def compare_password(self, password):
        # Compare the password
        return bcrypt.checkpw(password.encode('utf-8'), self.password)