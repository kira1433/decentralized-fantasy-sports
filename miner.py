from modules.blockchain import Block, Blockchain
from modules.transaction import Transactions, Transaction
from modules.user import Users
from modules.merkle import MerkleTree

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


                transaction_list = []
                transaction_list_bets = []

                for random_transaction in transactions:
                    if random_transaction.user not in [u.username for u in Users.get_users()]:
                        if Transactions.validate_transaction(random_transaction) and Transactions.verify_transaction(random_transaction):
                            print("Transaction validated and verified...")
                            transaction_list.append(random_transaction)
                            Transactions.successful_transaction(random_transaction)
                        else:
                            print("Invalid transaction")
                
                
                if(len(transaction_list) > 0):
                    transaction_list.append(Transaction('genesis', 'genesis', name, 5000.0, True, "#"))
                    mtree = MerkleTree(transaction_list)
                    mtreeRoot = mtree.getRoot()
                    dict_list = [t.to_dict() for t in transaction_list]
                    Blockchain.add_block(Block.create_block(dict_list, mtreeRoot), mtreeRoot)
                    

                for random_transaction in transactions:
                    if random_transaction.user in [u.username for u in Users.get_users()]:
                        if Transactions.validate_transaction(random_transaction) and Transactions.verify_transaction(random_transaction):
                            print("Transaction validated and verified...")
                            transaction_list_bets.append(random_transaction)
                            Transactions.successful_transaction(random_transaction)
                        else:
                            print("Invalid transaction")

                if(len(transaction_list_bets) > 0):
                    transaction_list_bets.append(Transaction('genesis', 'genesis', name, 5000.0, True, "#"))
                    mtree = MerkleTree(transaction_list_bets)
                    mtreeRoot = mtree.getRoot()
                    dict_list = [t.to_dict() for t in transaction_list_bets]
                    Blockchain.add_block(Block.create_block(dict_list, mtreeRoot), mtreeRoot)

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