import unittest

from entities.product import Product
from entities.product import ProductDiscountError

from entities.shopping_cart import ShoppingCart


class TestShoppingCart(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        pass
    
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    
    def setUp(self):
        self.name = 'iPhone'
        self.price = 500.00
        
        self.smathphone = Product(self.name, self.price)
        self.shopping_cart_1 = ShoppingCart()
        
        self.shopping_cart_2 = ShoppingCart()
        self.shopping_cart_2.add_product(self.smathphone)
        
    
    def tearDown(self):
        pass
    
        
    def test_shopping_cart_empty(self):
        self.assertTrue(self.shopping_cart_1.empty(), 'Lo sentimos, el carrito de compras no se encuentra vacío.')
    
    
    def test_shopping_cart_has_product(self):
        self.assertTrue(self.shopping_cart_2.has_products())
        self.assertFalse(self.shopping_cart_2.empty())
        
    
    def test_product_in_shopping_cart(self):
        product = Product('Nuevo producto', 10)
        self.shopping_cart_2.add_product(product)
        
        self.assertIn(product, self.shopping_cart_2.products)
        self.assertIn(self.smathphone, self.shopping_cart_2.products)
    
    
    def test_product_not_in_shopping_cart(self):
        self.shopping_cart_2.remove_product(self.smathphone)
        self.assertNotIn(self.smathphone, self.shopping_cart_2.products)
    
    
    def test_discount_error(self):
        with self.assertRaises(ProductDiscountError):
            Product(name='Example', price=10.0, discount=11.0)
    
    
    def test_total_shopping_cart(self):
        self.shopping_cart_1.add_product(Product(name='Libro', price=15.0))
        self.shopping_cart_1.add_product(Product(name='Cámara', price=700, discount=70))
        self.shopping_cart_1.add_product(Product(name='PC', price=1000, discount=0.0))
        
        self.assertGreater(self.shopping_cart_1.total, 0) # >
        self.assertLess(self.shopping_cart_1.total, 2000) # <
        
        self.assertEqual(self.shopping_cart_1.total, 1645.00)
        
        # assertGreaterEqual
        # assertLessEqual
        
    
    def test_total_empty_shopping_cart(self):
        self.assertEqual(self.shopping_cart_1.total, 0.0)
        
    
    # skipIf -> Evalua sobre Verdadero.
    # skipUnless -> Evalua sobre Falso.
    

    def test_code_product(self):
        self.assertRegex(self.smathphone.code, self.smathphone.name, 'Lo sentimos, el código no cumple con la expresión.') # Regex

