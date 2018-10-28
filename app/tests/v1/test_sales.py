import json
import unittest

from app.tests.v1.base_test import BaseTests


class SaleTests(BaseTests):
    """Tests functionality of the orders endpoint"""

    def test_create_sale(self):
        """Test API can create a sale"""
        access_token = self.user_token_get()
        self.client().post('/api/v1/products', data=self.add_product,
                                      content_type='application/json',
                           headers=dict(Authorization="Bearer " + access_token))
        response = self.client().post('/api/v1/sales', data=self.add_sale,
                                      content_type='application/json',
                                      headers=dict(Authorization="Bearer " + access_token))
        self.assertEqual(response.status_code, 201)

    def test_get_all_sales(self):
        """Tests API can get all products)"""
        access_token = self.user_token_get()
        sales= {"sales": "products"}
        response = self.client().get('/api/v1/sales', data=sales,
                                     content_type='application/json',
                                     headers=dict(Authorization="Bearer " + access_token))
        self.assertEqual(response.status_code, 200)

    def test_get_sale_by_id(self):
        """Tests API can get one product by using its id"""
        access_token = self.user_token_get()
        sales = {"sale_id": 1}
        self.client().post('/api/v1/products', data=self.add_product,
                           content_type='application/json',
                           headers=dict(Authorization="Bearer " + access_token))
        self.client().post('/api/v1/sales', data=self.add_sale,
                           content_type='application/json',
                           headers=dict(Authorization="Bearer " + access_token))
        response = self.client().get('/api/v1/sales/1', data=sales,
                                     content_type='application/json',
                                     headers=dict(Authorization="Bearer " + access_token)
                                     )
        self.assertEqual(response.status_code, 200)

    def test_get_incorrect_sale_id(self):
        access_token = self.user_token_get()

        """test invalid sale id"""
        sales = json.dumps({
            "sale_id": "1"
        })
        self.client().post('/api/v1/products', data=self.add_product,
                           content_type='application/json',
                            headers = dict(Authorization="Bearer " + access_token))
        self.client().post('/api/v1/sales', data=self.add_sale,
                           content_type='application/json',
                           headers=dict(Authorization="Bearer " + access_token))
        response= self.client().get ('/api/v1/sales/5', data= sales,
                                     content_type= 'application/json',
                                     headers=dict(Authorization="Bearer " + access_token))
        self.assertEqual(response.status_code, 404)

    def test_empty_product(self):
        """Test API can create a sale"""
        access_token = self.user_token_get()
        sales= {}
        response = self.client().post('/api/v1/sales', data=self.add_sale,
                                      content_type='application/json',
                                      headers=dict(Authorization="Bearer " + access_token))
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
