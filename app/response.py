from flask import jsonify, make_response


class Responses:
    """this class registers all my responses"""
    @staticmethod
    def complete_response(message):
        """this stores my response message"""
        response = make_response(jsonify({
            "Status": "OK",
            "Message": message,
        }), 200)
        return response
    @staticmethod
    def created_response (message):
        """this stores my successful resource creation"""
        response= make_response(jsonify({
            "Status":"Created successfully",
            "Message": message,
        }), 201)
        return response
    @staticmethod
    def not_found(message):
        """this returns not found messages"""
        response= make_response(jsonify({
            "Status":"Not found",
            "Message": message
        }), 404)
        return response
    @staticmethod
    def blank_input (message):
        """input your personal message here"""
        response= make_response(jsonify({
            "Status":"Empty field/s",
            "Message":message
        }), 404)
        return response
    @staticmethod
    def invalid_request(message):
        """this returns an invalid request message"""
        response = make_response(jsonify({
            "Status": "Bad Request",
            "Message": message
        }), 404)
        return response
    @staticmethod
    def error_message (message):
        response= make_response(jsonify({
            'Status': 'Error',
            'Message': message
        }), 400)
        return response

