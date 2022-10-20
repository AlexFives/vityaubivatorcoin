from transaction_db import TransactionDB

from decimal import Decimal
import time

db = TransactionDB(miner_user="Liza")

time.sleep(11)

db.make_transaction("Liza", "Alice", Decimal(10))

for transaction in db.transactions:
    print(transaction.sender, transaction.receiver, transaction.amount)
