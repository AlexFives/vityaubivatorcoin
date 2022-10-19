class NotEnoughCoins(Exception):
    def __init__(self, user: str):
        message = f"User {user} has not enough coins!"
        super().__init__(message)
