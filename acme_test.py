import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_weight(self):
      prod = Product('Test Product')
      self.assertEqual(prod.weight, 20)

    def test_default_flammability(self):
      prod = Product('Test Product')
      self.assertEqual(prod.flammability, 0.5)

    def test_prodcut_stealability(self):
      """"'Should return Very stealable!'"""
      prod = Product('Test Product', weight=5)
      self.assertEqual(prod.stealability(),"Very stealable!")


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_num(self):
        """Test default number of products."""
        products = generate_products()
        self.assertEqual(len(products), 30)

    #MOVE ON AND REVIST:
    # def test_legal_names(self):
    #   products = generate_products()
    #   product_names = []

    def test_average_price(self):
    """ Is this self referencing and pointless? """
      products = generate_products()
      Average_price = total_item_price/len(products)
      self.assertEqual(Average_price, total_item_price/len(products))


if __name__ == '__main__':
    unittest.main()