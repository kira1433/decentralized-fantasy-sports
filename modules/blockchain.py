import hashlib
import json
import time

class Block:
    def __init__(self, index=None, timestamp=None, data=None, previous_hash=None, nonce=0, hash=None):
        self.index = index or 0
        self.timestamp = timestamp or time.time()
        self.data = data or "Genesis Block"
        self.previous_hash = previous_hash or "0"
        self.nonce = nonce or 0
        self.hash = hash or self.calculate_hash()

    def __str__(self):
        return f"index: {self.index}, timestamp: {self.timestamp}, data: {self.data}"

    @staticmethod
    def create_block(data):
        transaction = {
            'sender': data['user'],
            'receiver': data['match'],
            'amount': data['amount']
        }
        return Block(data=transaction)
    
    def to_dict(self):
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce,
            'hash': self.hash
        }

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    #Proof of work
    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print("Block mined:", self.hash)


class Blockchain:
    chain = []
    difficulty = 4  # Adjust this value to increase/decrease mining difficulty

    @staticmethod
    def load_blockchain():
        with open("data.json", "r") as file:
            data = json.load(file)
            Blockchain.chain = [Block(**block) for block in data.get("blockchain", [])]

    @staticmethod
    def save_blockchain(blockchain):
        block_dicts = [block.to_dict() for block in blockchain]
        with open("data.json", "r") as file:
            data = json.load(file)
        data["blockchain"] = block_dicts
        with open("data.json", "w") as file:
            json.dump(data, file)

    @staticmethod
    def create_genesis_block():
        Blockchain.chain.append(Block(index=0, data={ "sender": "genesis", "receiver": "genesis", "amount": 0 }, previous_hash="0"))
        Blockchain.save_blockchain(Blockchain.chain)
    
    @staticmethod
    def get_latest_block():
        Blockchain.load_blockchain()
        return Blockchain.chain[-1]

    @staticmethod
    def add_block(new_block):
        Blockchain.load_blockchain()
        new_block.index = Blockchain.get_latest_block().index + 1
        new_block.previous_hash = Blockchain.get_latest_block().hash
        new_block.mine_block(Blockchain.difficulty)
        Blockchain.chain.append(new_block)
        Blockchain.save_blockchain(Blockchain.chain)

    @staticmethod
    def print_chain():
        Blockchain.load_blockchain()
        for block in Blockchain.chain:
            print(block)

    @staticmethod
    def is_chain_valid():
        Blockchain.load_blockchain()
        for i in range(1, len(Blockchain.chain)):
            current_block = Blockchain.chain[i]
            previous_block = Blockchain.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                print("Invalid block hash")
                return False

            if current_block.previous_hash != previous_block.hash:
                print("Invalid previous block hash")
                return False

        return True

    @staticmethod
    def get_balance(username):
        balance = 0
        Blockchain.load_blockchain()
        for block in Blockchain.chain:
            if block.data['receiver'] == username:
                balance += block.data['amount']
            if block.data['sender'] == username:
                balance -= block.data['amount']
        return balance
