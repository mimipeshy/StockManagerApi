import json
import unittest

from app.tests.v1.base_test import BaseTests


class SaleTests(BaseTests):
    """Tests functionality of the orders endpoint"""

    def test_create_sale(self):
        """Test API can create a sale"""
        add_sale = json.dumps({
            "product_name": "sugar",
            "quantity": 67,
            "price": 300
        })
        response = self.client().post('/api/v1/products', data=add_sale,
                                      content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_all_sales(self):
        """Tests API can get all products)"""
        sales= {"sales": "products"}
        response = self.client().get('/api/v1/products', data=sales,
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_sale_by_id(self):
        """Tests API can get one product by using its id"""
        sales = {"sale_id": "1"}
        response = self.client().get('/api/v1/products/1', data=sales,
                                     content_type='application/json',
                                     )
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()