from flask import request, jsonify
from flask_restful import Resource

from app.api.v1.models.products import *
from app.response import Responses


class AddProduct(Resource):

    @staticmethod
    def get():
        """this returns all products"""
        res = Responses.complete_response(products)
        return res

    def post(self):
        """this adds a new product"""
        data = request.get_json()
        product_name = data["product_name"]
        quantity = data["quantity"]
        price = data["price"]


        product = Product(product_name, quantity, price, )
        product.save()

        res = Responses.created_response(products)

        return res


class GetProduct(Resource):
    """this class deals with a single request"""

    def get(self, product_id):
        """this gets one product details"""
        for product in products:
            if product_id == product['product_id']:
                return jsonify({'product': product})
        return Responses.not_found("Product not found")

