# app/tests/v1/test_storeviews.py
import unittest
import json
from app import create_app
from .base_test import BaseTest

class TestStoreViews(BaseTest):
    def test_create_account(self):
        '''Test fetch for single sale record [GET request]'''
        resp=self.user_signup()
        result = json.loads(resp.data.decode('utf-8'))
        self.assertEqual(result['message'], 'Account created successfuly')
        self.assertEqual(resp.status_code, 201)

    '''Test for invalid email'''
    def test_invalid_email(self):
        '''Test fetch for single sale record [GET request]'''
        resp=self.check_invalid_email()
        result = json.loads(resp.data.decode('utf-8'))
        self.assertEqual(result['message'], 'invalid Email')
        self.assertEqual(resp.status_code, 401)

    '''Test for invalid password'''
    def test_invalid_password(self):
        resp=self.check_invalid_password()
        result = json.loads(resp.data.decode('utf-8'))
        self.assertEqual(result['message'], 'invalid password')
        self.assertEqual(resp.status_code, 401)

    '''Test Login'''
    def test_user_login(self):
        response = self.check_login()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200,result['message'])

    def test_add_existing_user(self):
        resp=self.signup_existing_user()
        result = json.loads(resp.data.decode('utf-8'))
        self.assertEqual(result['message'], ' marry@gmail.com Aready Exist')
        self.assertEqual(resp.status_code, 409)
    
    '''Test Login'''
    def test_user_login_with_invalid_password(self):
        response = self.login_with_invalid_password()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['message'],'Invalid Password')
        self.assertEqual(response.status_code, 200,result['message'])
    
    '''Test Login'''
    def test_user_login_with_invalid_email(self):
        response = self.login_with_invalid_email()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['message'],'Invalid Email. If have not account, register')
        self.assertEqual(response.status_code, 200)
      
    
 