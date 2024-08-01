from .product.py import Product

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        if not isinstance(product, Product):
            raise TypeError("Invalid product type")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        self.items.append((product, quantity))

    def total_price(self):
        return sum(item[0].price * item[1] for item in self.items)
