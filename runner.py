from modules.user import Users
from modules.transaction import Transactions

if __name__ == "__main__":
    name = input()
    key = input()
    if Users.login(name,key):
        for user in Users.get_users():
            print(user)

        print(f"Welcome {name}!")
        print("Enter the match you want to bet on:")
        match = input()
        print("Enter the team you want to bet on:")
        team = input()
        print("Enter the amount you want to bet:")
        amount = input()
        Transactions.add_transaction(name, team, match, amount)

        for transaction in Transactions.get_transactions():
            print(transaction)


        
