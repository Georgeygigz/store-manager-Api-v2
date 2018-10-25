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
        
    def test_get_all_products(self):
        response=self.get_all_products()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200,
                         result['Available Products'])

    '''Test add new product'''
    def test_add_new_product(self):
        response=self.add_new_product()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201, result['New Product'])

    '''Test fetch for specific product'''

    def test_fetch_single_product(self):
        '''Test fetch for single product [GET request]'''
        response=self.fetch_single_product()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200, result['Product'])

    '''Test Get all sales'''

    def test_get_all_sales(self):
        response=self.get_all_sales()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200, result['Sales Record'])

    ''' Test add new product'''

    def test_product_exist(self):
        resp=self.product_exist()
        result = json.loads(resp.data.decode('utf-8'))
        self.assertEqual(resp.status_code, 200, result["Sales Record"])

    def test_add_new_sale_record(self):
        response=self.add_new_product()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201, result['New Sale Record'])

    '''Test fetch for specific sale record'''

    def test_fetch_single_sale_record(self):
        resp=self.fetch_single_sale_record()
        result = json.loads(resp.data.decode('utf-8'))
        self.assertEqual(resp.status_code, 200, result['Sale'])

    def test_items_outof_range_record(self):
        '''Test fetch for single sale record [GET request]'''
        resp=self.items_outof_range_record()
        result = json.loads(resp.data.decode('utf-8'))
        self.assertEqual(result['Message'], 'Sale Not Found')
        self.assertEqual(resp.status_code, 400, result['Message'])
    
    def test_delete_products(self):
        response=self.delete_product()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 204,result['message'])

    '''Test invalid post url'''

    def test_invalid_post_product_url(self):
        response=self.invalid_post_product_url()
        self.assertEqual(response.status, '404 NOT FOUND')

    def test_invalid_get_product_url(self):
        response = self.invalid_get_product_url()
        self.assertEqual(response.status, '404 NOT FOUND')