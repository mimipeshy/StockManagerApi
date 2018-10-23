from datetime import date
sales= []
products=[]
total_price= 0

class Sale:
    """this initializes sales class methods"""
    def __init__(self, product_name, quantity, price, ):
        self.product_name= product_name
        self.quantity= quantity
        self.price= price
        self.sale_id= len(sales)+1
        self.date= str (date.today())
        self.product_id= len(products)+1

    def save (self):
        """this saves product data"""
        new_sale = {
            "sale_id":self.sale_id,
            "product_name": self.product_name,
            "product_id":self.product_id,
            "price":self.price,
            "quantity":self.quantity,
            "date":self.date
        }
        sales.append(new_sale)