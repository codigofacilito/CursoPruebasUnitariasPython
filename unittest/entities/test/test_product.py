import unittest

from entities.product import Product

class TestProduct(unittest.TestCase):
    
    def setUp(self):
        self.name = 'iPhone'
        self.price = 500.00
        
        self.smathphone = Product(self.name, self.price)
    
        
    def test_product_object(self):
        name = 'Manzana'
        price = 1.70
        
        product = Product(name, price)
        
        self.assertEqual(product.name, name)
        self.assertEqual(product.price, price, 'Lo sentimos, el precio no es el mismo.')
    
    
    def test_product_name(self):
        self.assertEqual(self.smathphone.name, self.name)
    
    
    def test_product_price(self):
        self.assertEqual(self.smathphone.price, self.price)
    