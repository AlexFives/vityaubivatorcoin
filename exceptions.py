class NotEnoughCoins(Exception):
    def __init__(self, user: str):
        message = f"User {user} has not enough coins!"
        super().__init__(message)


class TooLittleAmount(Exception):
    def __init__(self, amount: str):
        message = f"Amount {amount} is too small!"
        super().__init__(message)
