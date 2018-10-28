import json
import unittest

from app.tests.v1.base_test import BaseTests


class ProductTests(BaseTests):
    """Tests functionality of the orders endpoint"""

    def test_create_product(self):
        """Test API can create a product"""
        access_token = self.user_token_get()
        response = self.client().post('/api/v1/products', data=self.add_product,
                                      content_type='application/json',
                                      headers=dict(Authorization="Bearer " + access_token),
                                      )
        self.assertEqual(response.status_code, 201)

    def test_cannot_create_product(self):
        """test incorrect product creation"""
        access_token = self.user_token_get()
        response = self.client().post('/api/v1/products', data=self.bad_product,
                                      content_type='application/json',
                                      headers=dict(Authorization="Bearer " + access_token),
                                      )
        self.assertEqual(response.status_code, 404)

    def test_get_all_products(self):
        """Tests API can get all products)"""
        access_token = self.user_token_get()
        products = {"products": "products"}
        response = self.client().get('/api/v1/products', data=products,
                                     content_type='application/json',
                                     headers=dict(Authorization="Bearer " + access_token)
                                     )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())

    def test_get_product_by_id(self):
        """Tests API can get one product by using its id"""
        access_token = self.user_token_get()
        self.client().post('/api/v1/products', data=self.add_product,
                           content_type='application/json',
                           headers=dict(Authorization="Bearer " + access_token),
                           )

        response = self.client().get('/api/v1/products/1',
                                     content_type='application/json',
                                     headers=dict(Authorization="Bearer " + access_token)
                                     )
        self.assertEqual(response.status_code, 200)

    def test_invalid_id (self):
        """tests for an invalid product id"""
        access_token = self.user_token_get()
        self.client().post('/api/v1/products', data=self.add_product,
                           content_type='application/json',
                           headers=dict(Authorization="Bearer " + access_token),
                           )

        response = self.client().get('/api/v1/products/31',
                                     content_type='application/json',
                                     headers=dict(Authorization="Bearer " + access_token)
                                     )
        self.assertEqual(response.status_code, 404)

    def test_empty_string(self):
        """this tests for empty fields"""
        access_token = self.user_token_get()
        response = self.client().post('/api/v1/products', data=self.bad_product,
                                      content_type='application/json',
                                      headers=dict(Authorization="Bearer " + access_token),
                                      )
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
