import hashlib
import json
import time

class Block:
    def __init__(self, index=-1, data='', previous_hash=-1):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def __str__(self):
        return f"index: {self.index}, timestamp: {self.timestamp}, data: {self.data}"

    @staticmethod
    def create_block(data):
        return Block(data=data)

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
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 5  # Adjust this value to increase/decrease mining difficulty

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.index = self.get_latest_block().index + 1
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            print(block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                print("Invalid block hash")
                return False

            if current_block.previous_hash != previous_block.hash:
                print("Invalid previous block hash")
                return False

        return True

# Example usage:
if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.add_block(Block.create_block("Transaction 1"))
    blockchain.add_block(Block.create_block("Transaction 2"))
    blockchain.add_block(Block.create_block("Transaction 3"))

    print("Is blockchain valid?", blockchain.is_chain_valid())
    blockchain.print_chain()
