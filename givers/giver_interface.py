from abc import ABC, abstractmethod
from decimal import Decimal


class GiverInterface(ABC):
    @abstractmethod
    def get_reward(self) -> Decimal:
        ...
