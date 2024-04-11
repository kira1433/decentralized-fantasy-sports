import hashlib
import datetime as date

class Transaction:
    def __init__(self, user, team, match, amount):
        self.user = user
        self.team = team
        self.match = match
        self.amount = amount
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        transaction_string = f"{self.user}{self.team}{self.match}{self.amount}"
        return hashlib.sha256(transaction_string.encode()).hexdigest()

    def verify_transaction(self, public_key):
        # Implement HMAC Challenge-Response Authentication here
        # Generate a random challenge
        challenge = generate_challenge()

        # Send the challenge to the sender
        # The sender should respond with an HMAC response using their private key

        # Receive the response from the sender
        response = receive_response()

        # Verify the response using the sender's public key
        return verify_response(challenge, response, public_key)

class Block:
    def __init__(self, index, timestamp, transactions, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        transaction_hashes = "".join([tx.hash for tx in self.transactions])
        hash_string = str(self.index) + str(self.timestamp) + transaction_hashes + str(self.previous_hash)
        return hashlib.sha256(hash_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, date.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def mine_block(self):
        latest_block = self.get_latest_block()
        new_block = Block(latest_block.index + 1, date.datetime.now(), self.transactions, latest_block.hash)
        self.add_block(new_block)
        self.transactions = []

# Create the blockchain
blockchain = Blockchain()

# Add blocks to the blockchain
blockchain.add_block(Block(1, date.datetime.now(), "Transaction Data 1", ""))
blockchain.add_block(Block(2, date.datetime.now(), "Transaction Data 2", ""))
blockchain.add_block(Block(3, date.datetime.now(), "Transaction Data 3", ""))

# Print the contents of the blockchain
for block in blockchain.chain:
    print("Block #" + str(block.index))
    print("Timestamp: " + str(block.timestamp))
    print("Data: " + block.data)
    print("Hash: " + block.hash)
    print("Previous Hash: " + block.previous_hash)
    print("\n")