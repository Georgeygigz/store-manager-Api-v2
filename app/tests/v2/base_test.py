# app/tests/v1/base_test.py
import unittest
import json
import jwt
from app import create_app

'''Creating a new testing  class'''

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True
        self.products = {
            "product_id": 1,
            "product_name": "Bread",
            "category_id": 1,
            "stock_amount": 2000,
            "price": 20,
            "low_inventory_stock": 2
        }
        self.sales = {
            "sale_id": 1,
            "attedant_name": "Mary",
            "customer_name": "James",
            "product_name": "Bread",
            "product_price": 20,
            "quantity": 3,
            "total_price": 60,
            "date_sold": "12-3-2018"}

        self.user = {
            "user_id": 1,
            "username": 'mary',
            "email": "mary@gmail.com",
            "password": "maR#@Y_123",
            "role": "user"
        }
        self.user1 = {
            "email": "mary@gmail.com",
            "password": "maR#@Y_123",
        }


    def register_user(self):
        return self.app.post(
            '/api/v1/auth/register',
            data=json.dumps(self.user),
            content_type='application/json')

    def user_login(self):
        self.register_user()
        response = self.app.post('/api/v1/auth/login',
                                 data=json.dumps(self.user1))
        result = json.loads(response.data.decode('utf-8'))
        return result

    def get_user_token(self):
        '''Generate Token'''
        resp_login = self.user_login()
        token = resp_login.get("token")

        return token

    '''Test get all products'''

    def get_all_products(self):
        access_token = self.get_user_token()
        response = self.app.get(
            '/api/v1/products',
            headers={"content_type": 'application/json',
                     "x-access-token": access_token}
        )
        
        return response
    '''Test add new product'''

    def add_new_product(self):
        with self.app:
            access_token = self.get_user_token()
            response = self.app.post(
                '/api/v1/products',
                headers={"content_type": 'application/json',
                         "x-access-token": access_token},
                data=json.dumps(self.products))

            return response

    '''Test fetch for specific product'''

    def fetch_single_product(self):
        '''Test fetch for single product [GET request]'''
        with self.app:
            access_token = self.get_user_token()
            response = self.app.get(
                '/api/v1/products/1',
                headers={"content_type": 'application/json',
                         "x-access-token": access_token},
            )
            return response

    '''Test Get all sales'''

    def get_all_sales(self):
        access_token = self.get_user_token()
        response = self.app.get(
            '/api/v1/sales',
            headers={"content_type": 'application/json',
                     "x-access-token": access_token},
        )
        return response

    ''' Test add new product'''

    def product_exist(self):
        access_token = self.get_user_token()
        resp = self.app.get(
            '/api/v1/sales',
            headers={"content_type": 'application/json',
                     "x-access-token": access_token},
        )
        return resp

    def add_new_sale_record(self):
        access_token = self.get_user_token()
        response = self.app.post(
            '/api/v1/sales',
            data=json.dumps(self.sales),
            headers={"content_type": 'application/json',
                     "x-access-token": access_token},
        )
        return response

    '''Test fetch for specific sale record'''

    def fetch_single_sale_record(self):
        '''Test fetch for single sale record [GET request]'''
        access_token = self.get_user_token()
        resp = self.app.get(
            '/api/v1/sales/1',
            headers={"content_type": 'application/json',
                     "x-access-token": access_token},
        )
        return resp

    def items_outof_range_record(self):
        '''Test fetch for single sale record [GET request]'''
        access_token = self.get_user_token()
        resp = self.app.get(
            '/api/v1/sales/2',
            headers={"content_type": 'application/json',
                     "x-access-token": access_token},
        )
        return resp
    def delete_product(self):
        '''Test delete for a specific order API Endpoint [DELETE Request]''' 
        access_token = self.get_user_token()
        return self.app.delete('app/v1/products/1',
                                 headers={"content_type": 'application/json',
                                          "x-access-token": access_token},)
       

    '''Test invalid post url'''

    def invalid_post_product_url(self):
        response = self.app.post(
            '/api/v1/productss/',
            data=json.dumps(self.products),
            headers={'content_type': 'application/json'}
        )
        return response

    def invalid_get_product_url(self):
        response = self.app.get(
            '/api/v1//productss/',
            data=json.dumps(self.products),
            headers={'content_type': 'application/json'}
        )
        return response

    def user_create_account(self):
        return self.app.post(
            '/api/v1/auth/register',
            data=json.dumps(self.user),
            headers={'content_type': 'application/json'}
        )

    '''Test for invalid email'''
    def invalid_email(self):
        return self.app.post(
            'api/v1/auth/register',
            data=json.dumps(
                {"user_id": 1,
                 "username": 'mary',
                 "email": "marygmail.com",
                 "password": "maR#@Y_123",
                 "role": "user"}
            ),
            headers={'content_type': 'application/json'}
        )

    '''Test for invalid password'''
    def invalid_password(self):
        return self.app.post(
            'api/v1/auth/register',
            data=json.dumps(
                {"user_id": 1,
                 "username": 'mary',
                 "email": "mary@gmail.com",
                 "password": "maR#@",
                 "role": "user"}
            ),
            headers={'content_type': 'application/json'})
 


    '''Test Login'''
    def user_can_login(self):
        return self.app.post('/api/v1/auth/login', data=json.dumps(self.user ))
