from modules.user import Users
from modules.blockchain import Blockchain
from modules.transaction import Transactions
from modules.match import Matches

if __name__ == "__main__":
    print("Enter your username:")
    name = input()
    print("Enter your secret_key:")
    key = input()
    while key == "-1":
        print("Key cannot be -1")
        key = input()
        
    if Users.login(name,key):
        print(f"Welcome {name}!")
        while True:
            print("1. View matches")
            print("2. Bet on a match")
            print("3. View transactions")
            print("4. View balance")
            print("5. Exit")
            
            choice = input("Enter your choice: ")
            if choice == "1":
                for match in Matches.get_matches():
                    print(f"match_id:{match.match_id}, team_1: {match.team_1}, team_2: {match.team_2}\n")
            elif choice == "2":
                print("Enter the match_id you want to bet on:")
                match = input()
                print("Enter the team you want to bet on:")
                team = input()
                print("Enter the amount you want to bet:")
                amount = float(input())
                Transactions.add_transaction(name, team, match, amount,key)
            elif choice == "3":
                for transaction in Transactions.get_transactions():
                    if (transaction.user == name or transaction.match == name) and transaction.successful:
                        print(transaction)
            elif choice == "4":
                print(f"Your Balance is: {Blockchain.get_balance(name)}")
            elif choice == "5":
                exit()
    else:
        print("Invalid secret_key")
        exit()