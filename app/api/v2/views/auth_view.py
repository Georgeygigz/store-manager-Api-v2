# app/api/v1/views/auth_views.py
"""This is where all authentication Endpoints will be captured."""
import re
from flask_jwt_extended import (create_access_token, jwt_required,get_raw_jwt)
from flask import request, jsonify, make_response
import datetime
from functools import wraps
from passlib.hash import sha256_crypt

from flask_restful import Resource, reqparse

# import class products
from app.api.v2.models.auth_model import Users
from app.api.v2.utils.authorization import admin_required
blacklist = set()

def get_all_users():
    users=Users().get_all_users()
    return users
    
class CreateAccount(Resource):
    """Get all users."""
    @jwt_required
    @admin_required
    def get(self):
        if not get_all_users():
            return make_response(
                jsonify({"message": "No available users"}), 200)#ok
        return make_response(jsonify({"message":get_all_users()}), 200)#ok

        
    """Create a new account."""
    @jwt_required
    @admin_required
    def post(self):
        """Create an account for new user."""
        data = request.get_json(force=True)
        user_id = len(get_all_users()) + 1
        username = data["username"]
        email = data["email"]
        password = data["password"]
        role = data["role"]

        single_user = [user for user in get_all_users() if user['email']
                       == request.json['email']]
        if not re.match(
            r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$',
                request.json['email']):
            return make_response(jsonify({"message": "invalid Email"}), 400)#Bad request

        if not re.match(
            '(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$])',
                request.json['password']):
            return make_response(jsonify({"message": "invalid password"}), 400)#Bad request

        new_user_detail = {"user_id": user_id,
                           "username": username,
                           "email": email,
                           "password": sha256_crypt.hash(password),
                           "role": role}

        if not single_user:
            new_user = Users()
            new_user.insert_new_user(**new_user_detail)
            return make_response(
                jsonify({"message": "Account created successfuly"}), 201)#created

        return make_response(jsonify(
            {"message": " {} Aready Exist".format(request.json['email'])}), 409)  # conflict


class Login(Resource):
    """Login Endpoint."""

    def post(self):
        data = request.get_json(force=True)
        email = data['email']
        get_password = data['password']
        cur_user = [c_user for c_user in get_all_users() if c_user['email'] == email]

        if len(cur_user) > 0:
            password = cur_user[0]['password']
            if sha256_crypt.verify(get_password, password):
                token = create_access_token(identity=cur_user[0]['email'])
                result = {"message": "Login succesful","User":cur_user[0]['username'],"Role":cur_user[0]['role'], "token": token}

            else:
                return make_response(
                    jsonify({"message": "Incorrect Password"}), 401)#unauthorized
        else:
            return make_response(
                jsonify({"message": "Incorrect Email. If have not account, contact Admin"}), 401)#unauthorized

        return result, 200 #ok


class SingleUser(Resource):
    @jwt_required
    @admin_required
    def put(self, user_id):
        """Update user role."""
        data = request.get_json(force=True)
        role = (data["role"]).lower()
        update_user = [user for user in get_all_users() if user['user_id'] == user_id]
        if not update_user:
            return make_response(jsonify({'message': "User Not found"}), 400) #Bad request
        user = Users()
        user.update_user(user_id, role)
        return make_response(jsonify(
            {'message': "Updated Successfuly"}), 200) #ok
    
    
    @jwt_required
    @admin_required
    def delete(self, user_id):
        """Delete product user."""
        c_user = [
            current_user for current_user in get_all_users() if current_user['user_id'] == user_id]
        if not c_user:
            return make_response(jsonify({'message': "User Not found"}),  400) #Bad Request
        cur_user = Users()
        cur_user.delete_users(user_id)
        return make_response(jsonify({'message': "User Deleted Successfuly"}), 200) #ok

class Logout(Resource):
    @jwt_required
    def delete(self):
        jti = get_raw_jwt()['jti']
        blacklist.add(jti)
        return make_response(jsonify({"message": "Successfully logged out"}), 200)#ok
        