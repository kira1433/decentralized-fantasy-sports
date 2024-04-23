from modules.match import Matches
from modules.blockchain import Blockchain
from modules.transaction import Transactions
from modules.user import Users

if __name__ == "__main__":
    print("Enter match no:")
    match_id= 'match_' + input()
    print("Enter name of the first participating team")
    team_a=input()
    print("Enter name of the second participating team")
    team_b=input()
        
    Matches.create_match(match_id, team_a, team_b)
    for match in Matches.get_matches():
        print(match)

    print("Press Enter to continue")
    input()
    print("Enter name of winning team")
    winner=input()
    while(winner!=team_a and winner!=team_b):
        print("Enter Valid Team name")
        winner = input()

    total_pool = 0
    winner_pool = 0
    #calculate total pool and winner pool
    for transaction in Transactions.get_transactions():
        if transaction.match == match_id and transaction.successful:
            total_pool += int(transaction.amount)
            if transaction.team == winner:
                winner_pool += int(transaction.amount)
    #distribution of winning amount
    for transaction in Transactions.get_transactions():
        if transaction.match == match_id and transaction.successful and transaction.team == winner:
            secret_key=Users.fetch_secret_key(transaction.user)
            print("Adding credit transaction")
            Transactions.add_transaction(match_id, "winner", transaction.user, int(transaction.amount) * (total_pool / winner_pool),secret_key)
    
    Matches.remove_match(match_id)

    