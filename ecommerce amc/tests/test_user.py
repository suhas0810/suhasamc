import unittest
from src.product import Product
from src.cart import Cart
from src.user import User

class TestUser(unittest.TestCase):
    def test_purchase_success(self):
        user = User("Alice", 3000)
        cart = Cart()
        product = Product("Laptop", 1000, 5)
        cart.add_item(product, 2)
        total = user.purchase(cart)
        self.assertEqual(total, 2000)
        self.assertEqual(user.balance, 1000)

    def test_purchase_insufficient_balance(self):
        user = User("Alice", 1000)
        cart = Cart()
        product = Product("Laptop", 1000, 5)
        cart.add_item(product, 2)
        with self.assertRaises(ValueError):
            user.purchase(cart)

if __name__ == "__main__":
    unittest.main()
