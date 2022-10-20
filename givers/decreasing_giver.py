from .giver_interface import *


class DecreasingGiver(GiverInterface):
    def __init__(self,
                 base_reward: Decimal,
                 decrease_step: int,
                 decrease_on: Decimal):
        """

        :param base_reward: Самая первая награда.
        :param decrease_step: Каждые decrease_step награда уменьшается в decrease_on раз.
        :param decrease_on: Во сколько раз уменьшать награду.
        """
        self._reward = base_reward
        self._decrease_step = decrease_step
        self._decrease_on = decrease_on
        self.__iter = 0  # сколько одинаковых наград было выдано

    def get_reward(self) -> Decimal:
        if self.__iter == self._decrease_step:
            self.__iter = -1
            self._reward //= self._decrease_on
        self.__iter += 1
        return self._reward
