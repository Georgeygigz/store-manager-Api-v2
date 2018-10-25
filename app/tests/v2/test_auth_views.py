# app/tests/v1/test_storeviews.py
import unittest
import json
import jwt
from app import create_app
from .base_test import BaseTest

class TestStoreViews(BaseTest):
    def test_user_create_account(self):
        response =self.user_create_account()
        self.assertEqual(
            response.json, {'message': 'Account created successfuly'})
        self.assertEqual(response.status_code, 201)

    '''Test for invalid email'''
    def test_invalid_email(self):
        response = self.invalid_email()
        self.assertEqual(response.json, {'message': 'invalid Email'})
        self.assertEqual(response.status_code, 401)

    '''Test for invalid password'''
    def test_invalid_password(self):
        response = self.invalid_password()
        self.assertEqual(response.json, {'message': 'invalid password'})
        self.assertEqual(response.status_code, 401)

    '''Test Login'''
    def test_user_login(self):
        response = self.user_can_login()
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200,result['message'])
