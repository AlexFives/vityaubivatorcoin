from transaction import Transaction
from exceptions import *
from givers import DecreasingGiver

from typing import List, Iterator
from decimal import Decimal
import threading
import time


class TransactionDB:
    __GIVING_INTERVAL = 10

    def __init__(self,
                 miner_user: str,
                 min_transaction_amount: Decimal = Decimal(1e-3)):
        self.__miner_user = miner_user
        self.__transactions: List[Transaction] = list()
        self.__min_transaction_amount = min_transaction_amount
        self.__giver = DecreasingGiver(
            base_reward=Decimal(7200),
            decrease_step=12,
            decrease_on=Decimal(2)
        )
        self.__run_giving_thread()

    def __run_giving_thread(self):
        giving_thread = threading.Thread(target=self.__giving_loop, daemon=True)
        giving_thread.start()

    def __giving_loop(self):
        while True:
            time.sleep(self.__GIVING_INTERVAL)
            reward = self.__giver.get_reward()
            self.__reward(reward)

    def __reward(self, reward: Decimal):
        if not reward:
            return
        self.__apply_transaction('', self.__miner_user, reward)

    def make_transaction(self, sender: str, receiver: str, amount: Decimal):
        # т.к. от пустой строки будут идти награды для майнера,
        # то нужно сделать такую проверку
        if not sender:
            raise UnknownUser(sender)
        if not receiver:
            raise UnknownUser(receiver)

        if amount < self.__min_transaction_amount:
            raise TooLittleAmount(str(amount))
        balance = self.get_balance(sender)
        if balance < amount:
            raise NotEnoughCoins(sender)
        self.__apply_transaction(sender, receiver, amount)

    def get_balance(self, user: str) -> Decimal:
        taken = self.__count_taken_balance(user)
        given = self.__count_given_balance(user)
        return taken - given

    def __count_taken_balance(self, user: str) -> Decimal:
        result = Decimal(0)
        for transaction in self.__transactions:
            if transaction.receiver == user:
                result += transaction.amount
        return result

    def __count_given_balance(self, user: str) -> Decimal:
        result = Decimal(0)
        for transaction in self.__transactions:
            if transaction.sender == user:
                result += transaction.amount
        return result

    def __apply_transaction(self, sender: str, receiver: str, amount: Decimal):
        transaction = Transaction(sender, receiver, amount)
        self.__transactions.append(transaction)

    @property
    def transactions(self) -> Iterator[Transaction]:
        for transaction in self.__transactions:
            yield transaction
