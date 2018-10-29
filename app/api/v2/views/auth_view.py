# app/api/v1/views/auth_views.py
"""This is where all authentication Endpoints will be captured."""
import re
from flask_jwt_extended import (create_access_token, jwt_required)
from flask import request,jsonify, make_response
import datetime
from functools import wraps
from passlib.hash import sha256_crypt

from flask_restful import Resource,reqparse

# import class products
from app.api.v2.models.store_model import Users
from app.api.v2.utils.utils import Validate
from app.api.v2.utils.authorization import admin_required

users =Users().get_all_users()

class CreateAccount(Resource):
    """Create a new account."""
    @jwt_required
    @admin_required
    def post(self):
        """Create an account for new user."""
        data = request.get_json(force=True)
        user_id = len(users)+1
        username = data["username"]
        email = data["email"]
        password = data["password"]
        role = data["role"]
        single_user=[user for user in users if user['email']==request.json['email']]
        if not re.match(r'^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$', request.json['email']):
            return make_response(jsonify({"message": "invalid Email"}), 401)

        if not re.match('(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$])', request.json['password']):
            return make_response(jsonify({"message": "invalid password"}), 401)

        new_user_detail = {"user_id": user_id,
                           "username": username,
                           "email": email,
                           "password": sha256_crypt.encrypt(password),
                           "role": role}
        
        if not single_user :
            new_user=Users()
            new_user.insert_new_user(**new_user_detail)
            return make_response(jsonify({"message": "Account created successfuly"}), 201)

        return make_response(jsonify({"Message": " {} Aready Exist".format(request.json['email'])}), 409)  # conflict

class Login(Resource):
    """Login Endpoint."""
    def post(self):
        data = request.get_json(force=True)
        email=data['email']
        get_password=data['password']
        cur_user=[c_user for c_user in users if c_user['email']==email]

        if  len(cur_user) > 0:		
            password =cur_user[0]['password']
            if sha256_crypt.verify(get_password, password):      
                token = create_access_token(identity=cur_user[0]['email'])
                result={"message":"Login succesful","token":token}
                
            else:
                return make_response(jsonify({"message":"Invalid Password"}))
        else:
            return make_response(jsonify({"message":"Invalid Email. If have not account, register"}))

        return result,200