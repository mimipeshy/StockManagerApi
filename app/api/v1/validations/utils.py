import re
import time
from werkzeug.security import generate_password_hash, check_password_hash
from app.response import Responses


class Utils:
    @staticmethod
    def valid_email(email):
        valid_email = re.compile('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        return email if valid_email.match(email) else "Please Input a valid email"

    @staticmethod
    def valid_password_checker(password):
        password_checker = re.match(r"^(?=.*[a-z])(?=.*[0-9]){6}", password)
        return password if password_checker else "Your password should contain numbers and letters"


    @staticmethod
    def check_hashed_password(password, hashed_password):
        """checks that password hashed is equal to given password"""
        return check_password_hash(password, hashed_password)


