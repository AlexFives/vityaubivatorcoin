from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Transaction:
    sender: str
    receiver: str
    amount: Decimal
