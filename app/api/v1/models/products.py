from datetime import date
products= []


class Product:
    """this initializes product class methods"""
    def __init__(self, product_name, quantity, price):
        self.product_name= product_name
        self.quantity= quantity
        self.price= price
        self.product_id= len(products)+1
        self.date= str (date.today())


    def save (self):
        """this saves product data"""
        new_product= {
            "product_id":self.product_id,
            "product_name": self.product_name,
            "price":self.price,
            "quantity":self.quantity,
            "date":self.date,

        }
        products.append(new_product)
