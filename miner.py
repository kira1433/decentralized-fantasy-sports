from modules.blockchain import Block, Blockchain
from modules.transaction import Transactions
from modules.user import Users

if __name__ == "__main__":
    print("Enter your username:")
    name = input()
    key = "-1"
    if Users.login(name,key):
        print(f"Welcome {name}!")
        while True:
            print("1. Mine block")
            print("2. Print blockchain")
            print("3. Validate blockchain")
            print("4. View balance")
            print("5. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                if len(Transactions.get_unsuccessful_transactions()) == 0:
                    print("No transactions to mine")
                    continue
                transactions = Transactions.get_unsuccessful_transactions()
                # random_transaction = transactions[0] 
                current_index = 0
                transaction_list = []
                for random_transaction in transactions:
                    if Transactions.validate_transaction(random_transaction) and Transactions.verify_transaction(random_transaction):
                        print("Transaction validated and verified...")
                        transaction_list.append(random_transaction.to_dict())
                        # Blockchain.add_block(Block.create_block(random_transaction.to_dict()))
                        Transactions.successful_transaction(random_transaction)
                    else:
                        print("Invalid transaction")
                    current_index += 1
                if(len(transaction_list) > 0):
                    Blockchain.add_block(Block.create_block(transaction_list))
            elif choice == "2":
                Blockchain.print_chain()
            elif choice == "3":
                print("Blockchain is valid" if Blockchain.is_chain_valid() else "Blockchain is invalid")
            elif choice == "4":
                print(f"Your Balance is: {Blockchain.get_balance(name)}")
            elif choice == "5":
                exit()
    else:
        print("Invalid Miner")
        exit()