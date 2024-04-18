import hmac 
import hashlib
from modules.user import Users

def create_hmac(secret_key,message):
    hmac_obj = hmac.new(secret_key.encode(), msg=message.encode(), digestmod=hashlib.sha256)
    
    return hmac_obj.hexdigest()

def verify_hmac(secret_key,message,received_hmac):
    expected_hmac=create_hmac(secret_key=secret_key,message=message)
    return hmac.compare_digest(received_hmac, expected_hmac)

def verify_transaction_hmac(transaction):
    secret_key="#"
    if transaction.user=="genesis" or transaction.team=="winner":
        secret_key=Users.fetch_secret_key(transaction.match)
    else:
        secret_key=Users.fetch_secret_key(transaction.user)
    transaction_encoded=transaction.user+transaction.team+transaction.match+str(transaction.amount)
    received_hmac=transaction.transaction_hash
    return verify_hmac(secret_key=secret_key,message=transaction_encoded,received_hmac=received_hmac)
    