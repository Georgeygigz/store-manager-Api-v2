#app/tests/v2/test_models.py
'''
 Test case for our data storage
'''
import unittest
from app import create_app
from app.api.v2.models.store_model import (Products,Sales,Users)

class TestProductsModels(unittest.TestCase):
    '''Test for products class  and methods'''
    def setUp(self):
        """Set up the model."""
        self.products=Products()
        self.sales=Sales()
        self.available_users=Users()


    def test_available_data(self):
        """Test for available records."""
        # self.assertEqual(self.products.get_all_products(),[])
        # self.assertEqual(self.sales.get_all_sales(),[])
        # self.assertEqual(self.available_users.get_all_users(),[])
        pass
        
