
from flask_restful import abort


class Product_validation:
    """this verifies edge cases"""

    def empty_fields(self, product_name, price, quantity):

        if product_name == "" or  price == "" or quantity == "" :
            res = 'Fill in the product details'
            abort (400)
            return res


