# app/api/v1/views/store_views.py

'''This is where all API Endpoints will be captured'''
from flask import request, jsonify, make_response
from datetime import date
from flask_restful import Resource

# local imports
from app.api.v2.models.store_model import Products



products = Products().get_all_products()

class ViewProducts(Resource):
    '''Get all products'''
    def get(self):
        if not products:
            return make_response(jsonify({"Message": "No Available products"}), 200)
        return make_response(jsonify({"Available Products": products}), 200)
    

'''Fetch single product'''
class ViewSingleProduct(Resource):
    def get(self,product_id):
        single_product = [
            product for product in products if product['product_id'] == product_id]
        if not single_product:
            return {"Error": "Product Not Found"}, 404  # Not found
        return {"Product": single_product}, 200  # ok
