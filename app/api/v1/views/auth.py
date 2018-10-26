import re

from flask import request, jsonify, make_response, Flask
from flask_jwt_extended import create_access_token
from flask_restful import Resource

from app.api.v1.models.users import users
from app.response import Responses


class Signup(Resource):
    def post(self):
        """this class registers a new user"""
        data = request.get_json()
        email = data['email']
        password = data['password']

        if email == "" or password == "" or email == " " or password == " ":
            return Responses.blank_input("Please fill in the empty fields")

        email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

        if not re.match(email_regex, email):
            return Responses.error_message("invalid email")

        user = [user for user in users if user["email"] == email]
        if user:
            return Responses.invalid_request("User already exists, please login")

        user = {
            'id': len(users) + 1,
            'email': email,
            'password': password
        }
        users.append(user)
        return Responses.created_response(user)


