# app/tests/v1/base_test.py
import unittest
import json
import jwt
from app import create_app
from app.store_database import create_table, destory

'''Creating a new testing  class'''


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True
        create_table()
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
        self.invalid_product_values = {
            "product_id": 1,
            "product_name": "",
            "category_id": 1,
            "stock_amount": 2000,
            "price": 20,
            "low_inventory_stock": 2
        }
        self.invalid_product_keys = {
            "product_id": 1,
            "product_na": "Bread",
            "category_id": 1,
            "stock_amount": 2000,
            "price": 20,
            "low_inventory_stock": 2
        }
        self.invalid_sales_value = {
            "sale_id": 1,
            "attedant_name": "",
            "customer_name": "James",
            "product_name": "Bread",
            "product_price": 20,
            "quantity": 3,
            "total_price": 60,
            "date_sold": "12-3-2018"
        }
        self.invalid_sales_key = {
            "sale_id": 1,
            "attedant_na": "mary",
            "customer_name": "James",
            "product_name": "Bread",
            "product_price": 20,
            "quantity": 3,
            "total_price": 60,
            "date_sold": "12-3-2018"
        }
        self.invlaid_user_value = {
            "user_id": 1,
            "username": 'mary',
            "email": "mary@gmail.com",
            "password": "maR#@Y_123",
            "role": "user"
        }
        self.invlaid_user_keys = {
            "user_id": 1,
            "username": 'mary',
            "emai": "mary@gmail.com",
            "password": "maR#@Y_123",
            "role": "user"
        }
        self.invalid_login = {
            "email": "mary@gmail.com",
            "password": "maR#@Y_123",
        }

    def register_user(self):
        return self.app.post(
            '/api/v2/auth/register',
            data=json.dumps(self.user),
            content_type='application/json')

    def user_login(self):
        self.register_user()
        response = self.app.post('/api/v2/auth/login',
                                 data=json.dumps(self.user1))
        result = json.loads(response.data.decode('utf-8'))
        return result

    def get_user_token(self):
        '''Generate Token'''
        resp_login = self.user_login()
        token = resp_login.get("token")

        return token

    def get_all_products(self):
        """Test get all products."""
        access_token = self.get_user_token()
        response = self.app.get(
            '/api/v2/products',
            headers={"content_type": 'application/json',
                     "Authorization": 'Bearer ' + access_token}
        )

        return response

    def add_new_product(self):
        """Test add new product."""
        with self.app:
            access_token = self.get_user_token()
            response = self.app.post(
                '/api/v2/products',
                headers={"content_type": 'application/json',
                         "Authorization": 'Bearer ' + access_token},
                data=json.dumps(self.products))

            return response

    def fetch_single_product(self):
        '''Test fetch for single product [GET request]'''
        with self.app:
            access_token = self.get_user_token()
            response = self.app.get(
                '/api/v2/products/1',
                headers={"content_type": 'application/json',
                         "Authorization": 'Bearer ' + access_token},
            )
            return response

    def get_all_sales(self):
        """Test Get all sales."""
        access_token = self.get_user_token()
        response = self.app.get(
            '/api/v2/sales',
            headers={"content_type": 'application/json',
                     "Authorization": 'Bearer ' + access_token},
        )
        return response

    def product_exist(self):
        """Test add new product."""
        access_token = self.get_user_token()
        resp = self.app.get(
            '/api/v2/sales',
            headers={"content_type": 'application/json',
                     "Authorization": 'Bearer ' + access_token},
        )
        return resp

    def add_new_sale_record(self):
        """Add new sale record."""
        access_token = self.get_user_token()
        response = self.app.post(
            '/api/v2/sales',
            data=json.dumps(self.sales),
            headers={"content_type": 'application/json',
                     "Authorization": 'Bearer ' + access_token},
        )
        return response

    def fetch_single_sale_record(self):
        """Test fetch for single sale record [GET request]."""
        access_token = self.get_user_token()
        resp = self.app.get(
            '/api/v2/sales/1',
            headers={"content_type": 'application/json',
                     "Authorization": 'Bearer ' + access_token},
        )
        return resp

    def items_outof_range_record(self):
        """Test fetch for single sale record [GET request]."""
        access_token = self.get_user_token()
        resp = self.app.get(
            '/api/v2/sales/2',
            headers={"content_type": 'application/json',
                     "Authorization": 'Bearer ' + access_token},
        )
        return resp

    def delete_product(self):
        """Test delete for a specific order API Endpoint [DELETE Request]."""
        access_token = self.get_user_token()
        return self.app.delete('app/v2/products/1',
                               headers={"content_type": 'application/json',
                                        "Authorization": 'Bearer ' + access_token},)

    def invalid_post_product_url(self):
        """Test invalid post url."""
        response = self.app.post(
            '/api/v2/productss/',
            data=json.dumps(self.products),
            headers={'content_type': 'application/json'}
        )
        return response

    def invalid_get_product_url(self):
        response = self.app.get(
            '/api/v2//productss/',
            data=json.dumps(self.products),
            headers={'content_type': 'application/json'}
        )
        return response

    def user_create_account(self):
        return self.app.post(
            '/api/v2/auth/register',
            data=json.dumps(self.user),
            headers={'content_type': 'application/json'}
        )

    def invalid_email(self):
        """Test for invalid email."""
        return self.app.post(
            'api/v2/auth/register',
            data=json.dumps(
                {"user_id": 1,
                 "username": 'mary',
                 "email": "marygmail.com",
                 "password": "maR#@Y_123",
                 "role": "user"}
            ),
            headers={'content_type': 'application/json'}
        )

    def invalid_password(self):
        """Test for invalid password."""
        return self.app.post(
            'api/v2/auth/register',
            data=json.dumps(
                {"user_id": 1,
                 "username": 'mary',
                 "email": "mary@gmail.com",
                 "password": "maR#@",
                 "role": "user"}
            ),
            headers={'content_type': 'application/json'})

    def user_can_login(self):
        """Test Login."""
        return self.app.post('/api/v2/auth/login', data=json.dumps(self.user))

    def invalid_prodcut_field_name(self):
        with self.app:
            access_token = self.get_user_token()
            response = self.app.post(
                '/api/v2/products',
                headers={"content_type": 'application/json',
                         "Authorization": 'Bearer ' + access_token},
                data=json.dumps(self.invalid_product_values))

            return response

    def invalid_product_key_name(self):
        with self.app:
            access_token = self.get_user_token()
            response = self.app.post(
                '/api/v2/products',
                headers={"content_type": 'application/json',
                         "Authorization": 'Bearer ' + access_token},
                data=json.dumps(self.invalid_product_keys))

            return response

    def invalid_sales_field_name(self):
        access_token = self.get_user_token()
        response = self.app.post(
            '/api/v2/sales',
            data=json.dumps(self.invalid_sales_value),
            headers={"content_type": 'application/json',
                     "Authorization": 'Bearer ' + access_token},
        )
        return response

    def invalid_sales_key_name(self):
        access_token = self.get_user_token()
        response = self.app.post(
            '/api/v2/sales',
            data=json.dumps(self.invalid_sales_key),
            headers={"content_type": 'application/json',
                     "Authorization": 'Bearer ' + access_token},
        )
        return response

    def invalid_user_field_name(self):
        return self.app.post(
            '/api/v2/auth/register',
            data=json.dumps(self.invlaid_user_value),
            content_type='application/json')

    def invalid_user_key_name(self):
        return self.app.post(
            '/api/v2/auth/register',
            data=json.dumps(self.invlaid_user_keys),
            content_type='application/json')

    def update_product(self):
        pass

    
    def add_category(self):
        pass
    
    def update_category(self):
        pass
    
    def delete_category(self):
        pass

    def tearDown(self):
        destory()