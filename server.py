import json
from modules.blockchain import Blockchain

Blockchain.create_genesis_block()
if __name__ == "__main__":
    print("Press Enter to continue")
    input()
    with open("data.json", "w") as file:
        json.dump({"transactions": [], "users": [], "matches": [], "blockchain": []}, file)