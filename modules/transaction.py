import json
from modules.blockchain import Blockchain

class Transaction:
    def __init__(self, user, team, match, amount,successful=False):
        self.user = user
        self.team = team
        self.match = match
        self.amount = amount
        self.successful = successful

    def __str__(self):
        return f"user: {self.user}, match: {self.match}, team: {self.team}, amount: {self.amount}, successful: {self.successful}"

    def to_dict(self):
        return {
            'user': self.user,
            'match': self.match,
            'team': self.team,
            'amount': self.amount,
            'successful': self.successful
        }

class Transactions:
    @staticmethod
    def load_transactions():
        with open("data.json", "r") as file:
            data = json.load(file)
            return [Transaction(**transaction) for transaction in data.get("transactions", [])]
    
    @staticmethod
    def save_transactions(transactions):
        transaction_dicts = [transaction.to_dict() for transaction in transactions]
        with open("data.json", "r") as file:
            data = json.load(file)
        data["transactions"] = transaction_dicts
        with open("data.json", "w") as file:
            json.dump(data, file)
    
    @staticmethod
    def add_transaction(user, team, match, amount):
        transactions = Transactions.load_transactions()
        transactions.append(Transaction(user=user, team=team, match=match, amount=amount))
        Transactions.save_transactions(transactions)

    @staticmethod
    def successful_transaction(transaction):
        transactions = Transactions.load_transactions()
        for t in transactions:
            if t.user == transaction.user and t.match == transaction.match and t.team == transaction.team and t.amount == transaction.amount:
                t.successful = True
        Transactions.save_transactions(transactions)

    @staticmethod
    def get_transactions():
        return Transactions.load_transactions()
    
    @staticmethod
    def get_unsuccessful_transactions():
        return [transaction for transaction in Transactions.load_transactions() if not transaction.successful]

    @staticmethod
    def remove_transaction(remove_transaction):
        transactions = Transactions.load_transactions()
        transactions = [transaction for transaction in transactions if transaction.user != remove_transaction.user or transaction.match != remove_transaction.match or transaction.team != remove_transaction.team or transaction.amount != remove_transaction.amount]
        Transactions.save_transactions(transactions)

    @staticmethod
    def validate_transaction(transaction):
        if transaction.user == "genesis" or Blockchain.get_balance(transaction.user) >= transaction.amount: 
            return True
        Transactions.remove_transaction(transaction)
        return False
    
    @staticmethod
    def verify_transaction(transaction):
        pass
        