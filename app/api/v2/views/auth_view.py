# app/api/v1/views/auth_views.py
"""This is where all authentication Endpoints will be captured."""
import re
from flask_jwt_extended import (create_access_token, jwt_required)
from flask import request, jsonify, make_response
import datetime
from functools import wraps
from passlib.hash import sha256_crypt

from flask_restful import Resource, reqparse

# import class products
from app.api.v2.models.store_model import Users
from app.api.v2.utils.authorization import admin_required


class CreateAccount(Resource):
    """Create a new account."""
    @jwt_required
    @admin_required
    def post(self):
        """Create an account for new user."""
        users = Users().get_all_users()
        data = request.get_json(force=True)
        user_id = len(users) + 1
        username = data["username"]
        email = data["email"]
        password = data["password"]
        role = data["role"]

        single_user = [user for user in users if user['email']
                       == request.json['email']]
        if not re.match(
            r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$',
                request.json['email']):
            return make_response(jsonify({"message": "invalid Email"}), 401)

        if not re.match(
            '(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$])',
                request.json['password']):
            return make_response(jsonify({"message": "invalid password"}), 401)

        new_user_detail = {"user_id": user_id,
                           "username": username,
                           "email": email,
                           "password": sha256_crypt.hash(password),
                           "role": role}

        if not single_user:
            new_user = Users()
            new_user.insert_new_user(**new_user_detail)
            return make_response(
                jsonify({"message": "Account created successfuly"}), 201)

        return make_response(jsonify(
            {"message": " {} Aready Exist".format(request.json['email'])}), 409)  # conflict


class Login(Resource):
    """Login Endpoint."""

    def post(self):
        users = Users().get_all_users()
        data = request.get_json(force=True)
        email = data['email']
        get_password = data['password']
        cur_user = [c_user for c_user in users if c_user['email'] == email]

        if len(cur_user) > 0:
            password = cur_user[0]['password']
            if sha256_crypt.verify(get_password, password):
                token = create_access_token(identity=cur_user[0]['email'])
                result = {"message": "Login succesful", "token": token}

            else:
                return make_response(
                    jsonify({"message": "Incorrect Password"}), 401)
        else:
            return make_response(
                jsonify({"message": "Incorrect Email. If have not account, contact Admin"}), 401)

        return result, 200


class UpdateUserRole(Resource):
    @jwt_required
    @admin_required
    def put(self, user_id):
        """Update user role."""
        users = Users().get_all_users()
        data = request.get_json(force=True)
        role = (data["role"]).lower()
        update_user = [user for user in users if user['user_id'] == user_id]
        if not update_user:
            return make_response(jsonify({'Error': "User Not found"}), 400)
        user = Users()
        user.update_user(user_id, role)
        return make_response(jsonify(
            {'Message': "{} Updated Successfuly".format(update_user[0]['username'])}), 200)
