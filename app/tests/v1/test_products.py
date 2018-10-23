import json
import unittest

from app.tests.v1.base_test import BaseTests


class ProductTests(BaseTests):
    """Tests functionality of the orders endpoint"""

    def test_create_product(self):
        """Test API can create a product"""
        response = self.client().post('/api/v1/products', data=self.add_product,
                                      content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_all_products(self):
        """Tests API can get all products)"""
        products = {"products": "products"}
        response = self.client().get('/api/v1/products', data=products,
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_product_by_id(self):
        """Tests API can get one product by using its id"""
        products = {"product_id": 1}
        response = self.client().get('/api/v1/products/1', data=products,
                                      content_type='application/json',
                                      )
        self.assertEqual(response.status_code, 200)

    def test_incorrect_id(self):
        products = {"product_id": 1}
        response = self.client().get('/api/v1/products/6', data=products,
                                     content_type='application/json',
                                     )
        self.assertEqual(response.status_code, 404)




if __name__ == '__main__':
    unittest.main()
