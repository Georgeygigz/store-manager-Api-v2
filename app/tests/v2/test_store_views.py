# app/tests/v1/test_storeviews.py
import unittest
import json
import jwt
from app import create_app
from .base_test import BaseTest

class TestStoreViews(BaseTest):
    def test_config(self):
        '''Test configurations'''
        self.assertEqual(self.app.testing, True)

    def test_add_existing_product(self):
        """Test existing product."""
        response=self.product_exist()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 401,result["message"])
    
    def test_add_products(self):
        response=self.add_new_product()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201, result['New Product'])
        
    def test_get_all_products(self):
        """Get products."""
        response=self.get_all_products()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200,result['message'])

    '''Test fetch for specific product'''

    def test_fetch_single_product(self):
        """Test fetch for single product [GET request]."""
        response=self.fetch_single_product()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 404, result['Error'])

    def test_get_all_sales(self):
        """Test Get all sales."""
        response=self.get_all_sales()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['message'],"No Available sales records")
        self.assertEqual(response.status_code, 200)


    def test_update_product_by_valid_user(self):
        """Test add new product."""
        resp=self.product_exist()
        result = json.loads(resp.data.decode('utf-8'))
        self.assertEqual(resp.status_code, 201,result['New Product'])

    def test_add_new_sale_record_by_inalid_user(self):
        """Add sale record by invalid user."""
        response=self.add_new_product()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 401,result['message'])

    def test_fetch_invlaid_sale_record(self):
        """Test fetch for specific sale record."""
        resp=self.fetch_single_sale_record()
        result = json.loads(resp.data.decode('utf-8'))
        self.assertEqual(resp.status_code, 400)

    def test_invalid_user_get_single(self):
        """Test fetch for single sale record [GET request]."""
        resp=self.items_outof_range_record()
        result = json.loads(resp.data.decode('utf-8'))
        self.assertEqual(result['message'], 'This activity can be completed by Admin only')
        self.assertEqual(resp.status_code, 401)
    
    def test_invalid_post_product_url(self):
        """Test invalid post url."""
        response=self.invalid_post_product_url()
        self.assertEqual(response.status, '404 NOT FOUND')

    def test_invalid_get_product_url(self):
        """Test invalid get url."""
        response = self.invalid_get_product_url()
        self.assertEqual(response.status, '404 NOT FOUND')
             

    def test_add_product_by_invalid_user(self):
        """ Test add product by invalid user."""
        response=self.add_new_product()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['message'],'This activity can be completed by Admin only')
        self.assertEqual(response.status_code, 401)
       