import json
from modules.transaction import Transactions

class User:
    def __init__(self, username, public_key):
        self.username = username
        self.public_key = public_key

    def __str__(self):
        return f"username: {self.username}, public_key: {self.public_key}"

    def to_dict(self):
        return {
            'username': self.username,
            'public_key': self.public_key
        }
    
class Users:
    @staticmethod
    def load_users():
        with open("data.json", "r") as file:
            data = json.load(file)
            return [User(**user) for user in data.get("users", [])]

    @staticmethod
    def save_users(users):
        user_dicts = [user.to_dict() for user in users]
        with open("data.json", "r") as file:
            data = json.load(file)
        data["users"] = user_dicts
        with open("data.json", "w") as file:
            json.dump(data, file)

    @staticmethod
    def create_user(username, public_key):
        users = Users.load_users()
        users.append(User(username=username, public_key=public_key))
        Users.save_users(users)

    @staticmethod
    def get_users():
        return Users.load_users()

    @staticmethod
    def login(username, public_key):
        users = Users.load_users()
        for user in users:
            if user.username == username:
                return user.public_key == public_key
        Users.create_user(username, public_key)

        Transactions.add_transaction("genesis", "genesis", username, 10000.0)
        return True