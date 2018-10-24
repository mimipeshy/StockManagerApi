from flask import request, jsonify, make_response
from flask_restful import Resource, abort

from app.api.v1.models.products import *
from app.response import Responses

from app.api.v1.validations.utils import Product_validation


class AddProduct(Resource):

    @staticmethod
    def get():
        """this returns all products"""
        res = Responses.complete_response(products)
        return res

    def post(self):
        """this adds a new product"""
        try:

            data = request.get_json()

            product_name = data ["product_name"]
            quantity = data["quantity"]
            price = data["price"]

            if Product_validation.empty_fields(self, product_name, price, quantity):
                raise TypeError("Field cannot be empty")

            product = Product(product_name, quantity, price)

            product.save()

            res  = Responses.created_response(products)
            return res
        except  Exception as error:
            return make_response(jsonify(
                {"error": "Please provide for all the fields. Missing field: "}), 400)


class GetProduct(Resource):
    """this class deals with a single request"""
    def get(self, product_id):
        """this gets one product details"""
        for product in products:
            if product_id == product['product_id']:
                return jsonify({'product': product})
        return Responses.not_found("Product not found")
