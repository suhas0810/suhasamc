import unittest
from src.product import Product

class TestProduct(unittest.TestCase):
    def test_purchase_success(self):
        product = Product("Laptop", 1000, 10)
        cost = product.purchase(5)
        self.assertEqual(cost, 5000)
        self.assertEqual(product.stock, 5)

    def test_purchase_insufficient_stock(self):
        product = Product("Laptop", 1000, 2)
        with self.assertRaises(ValueError):
            product.purchase(5)

if __name__ == "__main__":
    unittest.main()
