
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse

from app.api.v1.models.products import products, Product
from app.api.v1.validations.utils import Product_validation
from app.response import Responses


class AddProduct(Resource):

    @staticmethod
    @jwt_required
    def get():
        """this returns all products"""
        res = Responses.complete_response(products)
        return res

    @jwt_required
    def post(self):
        """this adds a new product"""
        try:

            data = request.get_json()
            product_name = data["product_name"]
            quantity = data["quantity"]
            price = data["price"]

            if Product_validation.empty_fields(self, product_name, price, quantity):
                raise TypeError

            product = Product(product_name, quantity, price)

            product.save()

            res = Responses.created_response(products)
            return res
        except Exception:
            return Responses.blank_input("Fill in the fields")


class GetProduct(Resource):
    """this class deals with a single request"""
    @jwt_required
    def get(self, product_id):
        """this gets one product details"""
        for product in products:
            if product_id == product['product_id']:
                return jsonify({'product': product})
        return Responses.not_found("Product not found")





