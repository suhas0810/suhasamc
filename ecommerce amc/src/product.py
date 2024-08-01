class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def purchase(self, quantity):
        if quantity > self.stock:
            raise ValueError("Not enough stock available")
        self.stock -= quantity
        return self.price * quantity
