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
        self.add_sale=json.dumps({
            'product_id': 1
        })

