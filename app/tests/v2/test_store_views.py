# app/tests/v1/test_storeviews.py
import unittest
import json
import jwt
from app import create_app
from .base_test import BaseTest

class TestStoreViews(BaseTest):
    def test_config(self):
        """Test configurations."""
        self.assertEqual(self.app.testing, True)  
        
    def test_get_all_products(self):
        """Test get all products."""
        response=self.get_all_products()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200,result['Available Products'] )

    def test_get_unexisting_products(self):
        """Test geet unexisting products."""
        response=self.get_unexisting_products()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['message'],"No Available products")
        self.assertEqual(response.status_code, 200)

    def test_add_new_product(self):
        """Test add new product."""
        response=self.add_new_product()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201, result['New Product'])
    
    def test_invalid_data_types(self):
        """Test invalid data types."""
        response=self.check_invalid_data_type()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['Error'],"Require int or float type")
        self.assertEqual(response.status_code, 200)

    def test_fetch_single_product(self):
        """Test fetch for single product [GET request]."""
        response=self.fetch_single_product()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200, result['Product'])

    def test_delete_product(self):
        """Test delete product."""
        response=self.delete_products()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['Message'],'Deleted Successfuly')
        self.assertEqual(response.status_code, 200)

    def test_delete_unexisting_product(self):
        """Test delete unexisting product."""
        response=self.delete_unexisting_products()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['Error'],'Product Not found')
        self.assertEqual(response.status_code, 400)

    def test_update_product(self):
        """Test update product."""
        response=self.update_products()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['Message'],'orange Updated Successfuly')
        self.assertEqual(response.status_code, 200)

    def test_add_new_sale_record(self):
        """Test add new sale record."""
        response=self.add_new_sale_record()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201,result['New Sale Record'])
    
    def test_add_an_existing_sale_record(self):
        """Test add new sale record."""
        response=self.check_sale_exist()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['Message'],'orange Exist in cart')
        self.assertEqual(response.status_code, 200)
    
    def test_make_sale_of_unexisting_product(self):
        """Test add new sale record."""
        response=self.make_sale_of_unexisting_product()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['Message'],'orange Out of stock')
        self.assertEqual(response.status_code, 200)

    def test_make_sale_of_exeding_amount_instock(self):
        """Test add new sale record."""
        response=self.make_sale_of_exeding_amount_instock()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['Message'],'Quantity exeed amount in stock')
        self.assertEqual(response.status_code, 200)

    def test_get_all_sales(self):
        """Test get all sales records."""
        response=self.get_all_sales()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200, result['Sales Record'])

    def test_fetch_single_sale_record(self):
        """Test fetch for single sale record [GET request]."""
        resp=self.fetch_single_sale_record()
        result = json.loads(resp.data.decode('utf-8'))
        self.assertEqual(resp.status_code, 200, result['Sale'])

    def test_items_outof_range_record(self):
        """Test get product that doesent eist."""
        resp=self.items_outof_range_record()
        result = json.loads(resp.data.decode('utf-8'))
        self.assertEqual(result['Message'], 'Sale Not Found')
        self.assertEqual(resp.status_code, 400, result['Message'])

    def test_invalid_post_product_url(self):
        """Test invalid post url."""
        response=self.invalid_post_product_url()
        self.assertEqual(response.status, '404 NOT FOUND')

    def test_invalid_get_product_url(self):
        """Test invalid get url."""
        response=self.invalid_get_product_url()
        self.assertEqual(response.status, '404 NOT FOUND')
