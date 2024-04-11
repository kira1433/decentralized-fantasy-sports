from modules.blockchain import Block, Blockchain
from modules.transaction import Transactions

if __name__ == "__main__":
    while True:
        print("1. Mine block")
        print("2. Print blockchain")
        print("3. Validate blockchain")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            transactions = Transactions.get_unsuccessful_transactions()
            random_transaction = transactions[0]
            if Transactions.validate_transaction(random_transaction):
                Blockchain.add_block(Block.create_block(random_transaction.to_dict()))
                Transactions.successful_transaction(random_transaction)
            else:
                print("Invalid transaction")
        elif choice == "2":
            Blockchain.print_chain()
        elif choice == "3":
            print("Blockchain is valid" if Blockchain.is_chain_valid() else "Blockchain is invalid")
        elif choice == "4":
            break
        else:
            print("Invalid choice")