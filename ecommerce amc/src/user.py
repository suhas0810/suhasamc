class User:
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

    def purchase(self, cart):
        total = cart.total_price()
        if self.balance < total:
            raise ValueError("Insufficient balance")
        self.balance -= total
        return total
