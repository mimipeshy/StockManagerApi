import jwt
from coverage.config import os
from flask import request, jsonify
from flask_restful import Resource
from werkzeug.security import check_password_hash

from app.api.v1.models.users import *
from app.response import Responses
from app.api.v1.validations.utils import Utils


class RegisterUser(Resource):

    def post(self):
        """this registers a new user"""
        data = request.get_json(force= True)
        email = data['email']
        password = data['password']
        new_user = {
            "user_id": len(users) + 1,
            "email": Utils.valid_email(email),
            "password": Utils.valid_password_checker(password),

        }
        users.append(new_user)
        return Responses.created_response(new_user)



