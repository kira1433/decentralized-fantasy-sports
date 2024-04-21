import json
import secrets
import random
import hmac
import hashlib

def create_hmac(secret_key,message):
    hmac_obj = hmac.new(secret_key.encode(), msg=message.encode(), digestmod=hashlib.sha256)
    
    return hmac_obj.hexdigest()

def verify_hmac(secret_key,message,received_hmac):
    expected_hmac=create_hmac(secret_key=secret_key,message=message)
    return hmac.compare_digest(received_hmac, expected_hmac)

class User:
    def __init__(self, username, secret_key):
        self.username = username
        self.secret_key = secret_key

    def __str__(self):
        return f"username: {self.username}, secret_key: {self.secret_key}"

    def to_dict(self):
        return {
            'username': self.username,
            'secret_key': self.secret_key
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
    def create_user(username, secret_key):
        users = Users.load_users()
        users.append(User(username=username, secret_key=secret_key))
        Users.save_users(users)

    @staticmethod
    def get_users():
        return Users.load_users()
    
    @staticmethod
    def fetch_secret_key(username):
        users=Users.load_users()
        for user in users:
            if user.username == username:
                return user.secret_key

    @staticmethod
    def login(username, secret_key):
        users = Users.load_users()
        for user in users:
            if user.username == username:
                return user.secret_key == secret_key
        Users.create_user(username, secret_key)

        random_challenge = secrets.token_hex(16)
        random_bit = random.randint(0,1)
        message = f"{random_challenge}{random_bit}"
        hash = create_hmac(secret_key, message)
        if not verify_hmac(secret_key, message, hash):
            print("HMAC verification failed")
            return False

        if secret_key=="-1":
            return True
        from modules.transaction import Transactions
        Transactions.add_transaction("genesis", "genesis", username, 10000.0,secret_key)
        return True