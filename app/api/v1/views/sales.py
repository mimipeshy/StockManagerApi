
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from app.api.v1.models.sales import *
from app.api.v1.models.products import *
from app.response import Responses


class MakeSales(Resource):

    @staticmethod
    @jwt_required
    def get():
        """this returns all sales"""
        res = Responses.complete_response(sales)
        return res

    @jwt_required
    def post(self):
        """this adds a new sale"""
        data = request.get_json()
        product_id = data ['product_id']

        for product in products:
            if product_id == int(product['product_id']):
                sale = {
                    'sale_id': len(sales) + 1,
                    'product': product
                }
                sales.append(sale)

                product['quantity'] = int(product['quantity']) - 1
                if product['quantity'] < 0:
                   return Responses.not_found("Product sold out")
            return Responses.created_response(sales)
        return Responses.not_found("Product not found")


class GetSale(Resource):
    """this class deals with a single request"""
    @jwt_required
    def get(self, sale_id):
        """this gets one product details"""
        for sale in sales:
            if sale_id == sale['sale_id']:
                return jsonify({'sale': sale})
        return Responses.not_found("Sale record not found")


