# app/api/v1/views/store_views.py

'''This is where all API Endpoints will be captured'''
from flask import request, jsonify, make_response
from datetime import date
from flask_restful import Resource

# local imports
from app.api.v2.models.store_model import Products
from app.api.v2.utils.utils import Validate



products = Products().get_all_products()

class ViewProducts(Resource):
    """Get all products."""
    def get(self):
        if not products:
            return make_response(jsonify({"Message": "No Available products"}), 200)
        return make_response(jsonify({"Available Products": products}), 200)

    """Add a new product."""    
    def post(self):
        data = request.get_json(force=True)
        Validate().validate_empty_product_inputs(data)  
        product_id = len(products)+1
        product_name = data["product_name"]
        category = data["category_id"]
        stock_amount = data["stock_amount"]
        price = data['price']
        inventory_stock = data['low_inventory_stock']
        product = [product for product in products if product['product_name']
                   == request.json['product_name']]
        if (not request.json or not "product_name" in request.json):
            return {'Error': "Request Not found"}, 404  # not found

        if type((request.json['stock_amount']) or (request.json['price'])) not in [int, float]:
            return {"Error": "Require int or float type"}

        if request.json['product_name'] in [n_product['product_name'] for n_product in products]:
            product[0]["stock_amount"] += request.json['stock_amount']
            return {"Products": product}, 200  # ok

        new_product = {
            "product_id": product_id,
            "product_name": product_name,
            "category_id": category,
            "stock_amount": stock_amount,
            "price": price,
            "low_inventory_stock": inventory_stock
        }

        new_pro=Products()
        new_pro.insert_new_product(**new_product)

        return {"New Product": new_product}, 201  # created
    

"""Fetch single product."""
class ViewSingleProduct(Resource):
    def get(self,product_id):
        single_product = [
            product for product in products if product['product_id'] == product_id]
        if not single_product:
            return {"Error": "Product Not Found"}, 404  # Not found
        return {"Product": single_product}, 200  # ok
