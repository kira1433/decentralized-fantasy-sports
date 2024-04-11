import json

class Transaction:
    def __init__(self, user, team, match, amount):
        self.user = user
        self.team = team
        self.match = match
        self.amount = amount

    def __str__(self):
        return f"user: {self.user}, match: {self.match}, team: {self.team}, amount: {self.amount}"

    def to_dict(self):
        return {
            'user': self.user,
            'match': self.match,
            'team': self.team,
            'amount': self.amount
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
    def remove_transaction(remove_transaction):
        transactions = Transactions.load_transactions()
        transactions = [transaction for transaction in transactions if transaction.user != remove_transaction.user or transaction.match != remove_transaction.match or transaction.team != remove_transaction.team or transaction.amount != remove_transaction.amount]
        Transactions.save_transactions(transactions)

    @staticmethod
    def get_transactions():
        return Transactions.load_transactions()
