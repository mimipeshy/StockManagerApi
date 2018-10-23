from datetime import datetime
users=[]

class User:
    """this initializes user class methods"""
    def __init__(self, email,password):
        self.email= email
        self.password= password
        self.date_registered=datetime.now()
        self.user_id= len(users)+1

