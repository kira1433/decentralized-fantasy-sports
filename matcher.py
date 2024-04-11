from modules.match import Matches
from modules.blockchain import Blockchain
from modules.transaction import Transactions

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
    total_pool = 0
    winner_pool = 0

    for transaction in Transactions.get_transactions():
        if transaction.match == match_id and transaction.successful:
            total_pool += int(transaction.amount)
            if transaction.team == winner:
                winner_pool += int(transaction.amount)

    for transaction in Transactions.get_transactions():
        if transaction.match == match_id and transaction.successful and transaction.team == winner:
            Transactions.add_transaction(match_id, "winner", transaction.user, int(transaction.amount) * (total_pool / winner_pool))
    
    
    