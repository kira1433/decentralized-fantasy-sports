import random
from server import blockchain
from modules.blockchain import Block
from modules.transaction import Transactions

if __name__ == "__main__":
    while True:
        print("1. Mine block")
        print("2. Print blockchain")
        print("3. Validate blockchain")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            transactions = Transactions.get_transactions()
            random_transaction = transactions[random.randint(0, len(transactions) - 1)]
            blockchain.add_block(Block.create_block(random_transaction.to_dict()))
            Transactions.remove_transaction(random_transaction)
        elif choice == "2":
            blockchain.print_chain()
        elif choice == "3":
            print("Blockchain is valid" if blockchain.is_chain_valid() else "Blockchain is invalid")
        elif choice == "4":
            break
        else:
            print("Invalid choice")