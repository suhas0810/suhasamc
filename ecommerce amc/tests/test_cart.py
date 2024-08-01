import unittest
from src.product import Product
from src.cart import Cart

class TestCart(unittest.TestCase):
    def test_add_item_success(self):
        product = Product("Laptop", 1000, 10)
        cart = Cart()
        cart.add_item(product, 2)
        self.assertEqual(len(cart.items), 1)
        self.assertEqual(cart.items[0], (product, 2))

    def test_add_item_invalid_product(self):
        cart = Cart()
        with self.assertRaises(TypeError):
            cart.add_item("Not a product", 2)

    def test_add_item_invalid_quantity(self):
        product = Product("Laptop", 1000, 10)
        cart = Cart()
        with self.assertRaises(ValueError):
            cart.add_item(product, -1)

    def test_total_price(self):
        product1 = Product("Laptop", 1000, 10)
        product2 = Product("Mouse", 50, 50)
        cart = Cart()
        cart.add_item(product1, 1)
        cart.add_item(product2, 2)
        self.assertEqual(cart.total_price(), 1100)

if __name__ == "__main__":
    unittest.main()
