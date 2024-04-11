from modules.user import Users
from modules.transaction import Transactions
from modules.match import Matches

if __name__ == "__main__":
    print("Enter your username:")
    name = input()
    print("Enter your public_key:")
    key = input()
    if Users.login(name,key):
        print(f"Welcome {name}! Here are the list of matches to bet on")
        
        for match in Matches.get_matches():
            print(f"ID:{match.match_id}, Team 1: {match.team_1}, Team 2: {match.team_2}")

        print("Enter the match id you want to bet on:")
        match = input()
        print("Enter the team you want to bet on:")
        team = input()
        print("Enter the amount you want to bet:")
        amount = input()
        
        Transactions.add_transaction(name, team, match, amount)


        
