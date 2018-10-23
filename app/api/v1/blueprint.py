from flask import Blueprint
from flask_restful import Api,Resource

from app.api.v1.views.products import AddProduct, GetProduct
from app.api.v1.views.sales import MakeSales, GetSale
from app.api.v1.views.auth import RegisterUser, Login

ns = Blueprint('api', __name__, url_prefix="/api/v1")
api = Api(ns)

api.add_resource(AddProduct, "/products")
api.add_resource(GetProduct, "/products/<int:product_id>")
api.add_resource(MakeSales, "/sales")
api.add_resource(GetSale, "/sales/<int:sale_id>")
api.add_resource(RegisterUser, '/auth/register')
api.add_resource(Login, '/auth/login')