import json
from modules.blockchain import Blockchain

blockchain = Blockchain()
if __name__ == "__main__":
    input()
    with open("data.json", "w") as file:
        json.dump({"transactions": [], "users": [], "matches": []}, file)