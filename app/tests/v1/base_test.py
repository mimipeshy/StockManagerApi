import unittest
import sys  # fix import errors
import os
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.app import create_app


class BaseTests(unittest.TestCase):
    """This class represents the base configurations for all tests"""

    def setUp(self):
        """Define test variables and initialize app"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

        self.add_product= json.dumps({
            "product_name":"sugar",
            "quantity":67,
            "price":300
        })
        self.bad_product = json.dumps({
            "product_name": "",
            "quantity": 67,
            "price": 300
        })
        self.add_sale=json.dumps({
            'product_id': 1
        })
        self.email_regex = json.dumps(({
            'email': "perisndanu@gmail.com",
            'password':"12345"
        }))

    def register_user(self, email, password,):
            """Register user with dummy data"""
            return self.client().post(
                '/api/v1/auth/register',
                content_type='application/json',
                data=json.dumps(dict(
                                     email=email,
                                     password=password,
                                     )))
    def login_user (self, email, password):
        """Register user with dummy data"""
        return self.client().post(
            '/api/v1/auth/login',
            content_type='application/json',
            data=json.dumps(dict(email=email, password=password)))

    def user_token_get(self):
        self.register_user("perisndanu@gmail.com", "12345")
        data = self.login_user("perisndanu@gmail.com", "12345")
        access_token = json.loads(data.data.decode())['token']
        return access_token

