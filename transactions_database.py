from decimal import Decimal
from typing import Iterator

from transaction import Transaction
from exceptions import NotEnoughCoins


class TransactionsDatabase:
    def __init__(self):
        self.__transactions = list()

    def make_transaction(self, sender_pkh: str, receiver: str, amount: Decimal):
        sender_balance = self.get_balance(sender_pkh)
        if sender_balance < amount:
            raise NotEnoughCoins(sender_pkh)
        self.__apply_transaction(sender_pkh, receiver, amount)

    def get_balance(self, pkh: str) -> Decimal:
        taken = self.__count_taken_coins(pkh)
        given = self.__count_given_coins(pkh)
        return taken - given

    def __count_taken_coins(self, sender_pkh: str) -> Decimal:
        taken = Decimal(0)
        for transaction in self.__transactions:
            if transaction.receiver == sender_pkh:
                taken += transaction.amount
        return taken

    def __count_given_coins(self, sender_pkh: str) -> Decimal:
        given = Decimal(0)
        for transaction in self.__transactions:
            if transaction.sender == sender_pkh:
                given += transaction.amount
        return given

    def __apply_transaction(self, sender_pkh: str, receiver_pkh: str, amount: Decimal):
        transaction = Transaction(sender_pkh, receiver_pkh, amount)
        self.__transactions.append(transaction)

    @property
    def transactions(self) -> Iterator[Transaction]:
        for transaction in self.__transactions:
            yield transaction
