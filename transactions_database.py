from decimal import Decimal
from typing import Iterator
import threading
import time

from transaction import Transaction
from exceptions import NotEnoughCoins, TooLittleAmount


class TransactionsDatabase:

    def __init__(self,
                 host_name: str,
                 root_user: str = 'root',
                 minimal_transaction_amount: Decimal = Decimal(1e-3)):
        self.__transactions = list()
        self.__run_miner_thread(host_name)
        self.__root_user = root_user
        self.__minimal_transaction_amount = minimal_transaction_amount

    def __run_miner_thread(self, host_name: str):
        miner_thread = threading.Thread(target=self.__miner_thread, args=(host_name,), daemon=True)
        miner_thread.start()

    def __miner_thread(self, host_name: str):
        previous_reward_time = 0.0
        while True:



    def make_transaction(self, sender_name: str, receiver_name: str, amount: Decimal):
        if amount <

        if sender_name == self.__root_user:
            # чтобы исключить возможность транзаций от пользователя с бесконечным балансом
            raise NotEnoughCoins(sender_name)

        sender_balance = self.get_balance(sender_name)
        if sender_balance < amount:
            raise NotEnoughCoins(sender_name)
        self.__apply_transaction(sender_name, receiver_name, amount)

    def get_balance(self, name: str) -> Decimal:
        taken = self.__count_taken_coins(name)
        given = self.__count_given_coins(name)
        return taken - given

    def __count_taken_coins(self, sender_name: str) -> Decimal:
        taken = Decimal(0)
        for transaction in self.__transactions:
            if transaction.receiver == sender_name:
                taken += transaction.amount
        return taken

    def __count_given_coins(self, sender_name: str) -> Decimal:
        given = Decimal(0)
        for transaction in self.__transactions:
            if transaction.sender == sender_name:
                given += transaction.amount
        return given

    def __apply_transaction(self, sender_name: str, receiver_name: str, amount: Decimal):
        transaction = Transaction(sender_name, receiver_name, amount)
        self.__transactions.append(transaction)

    @property
    def transactions(self) -> Iterator[Transaction]:
        for transaction in self.__transactions:
            yield transaction
