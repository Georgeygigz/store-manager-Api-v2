# app/api/v1/views/store_views.py

"""This is where all API Endpoints will be captured."""
from flask import request, jsonify, make_response
from datetime import date
from flask_restful import Resource
from flask_jwt_extended import (jwt_required, get_jwt_identity)

# local imports
from app.api.v2.models.products_model import (Products)
from app.api.v2.models.sales_model import (Sales)
from app.api.v2.models.auth_model import (Users)
from app.api.v2.models.category_model import (Categories)
from app.api.v2.utils.authorization import (
    admin_required, store_attendant_required)

def get_all_products():
    products = Products().get_all_products()
    return products


class ViewProducts(Resource):
    @jwt_required
    def get(self):
        """Get all products."""
        if not get_all_products():
            return make_response(
                jsonify({"message": "No Available products"}), 200) #Ok
        return make_response(jsonify({"message": get_all_products()}), 200) #Ok

    @jwt_required
    @admin_required
    def post(self):
        """Add a new product."""
        data = request.get_json(force=True)
        required_inputs = ['product_name', 'category_id','stock_amount', 'price', 'image']
        for field in required_inputs:
            if field not in request.json:
                return make_response(jsonify({'message': " {} missing".format(field)}))
        product_id = len(get_all_products()) + 1
        product_name = data["product_name"]
        category = data["category_id"]
        stock_amount = data["stock_amount"]
        price = data['price']
        image=data['image']
        empty_inputs = [product_name,category,stock_amount,price,image]
        for empty_field in empty_inputs:
            if (empty_field ==""):
                return make_response(jsonify({'message': "{} Empty field detected".format(empty_field)}))

        product = [product for product in get_all_products() if product['product_name']
                   == request.json['product_name']]

        if (not request.json or "product_name" not in request.json):
            return make_response(jsonify({'message': "Request Not found"}), 404)# Not Found

        if type(request.json['stock_amount'])not in [int, float]:
            return make_response(
                jsonify({"message": "Require int or float type"}))

        if request.json['product_name'] in [
                n_product['product_name'] for n_product in get_all_products()]:
            product[0]["stock_amount"] += request.json['stock_amount']
            update_product = Products()
            update_product.update_stock_amount(
                product[0]['product_name'], product[0]['stock_amount'])
            return make_response(jsonify({"message": "Product updated successfully"}), 200)  # ok

        new_product = {
            "product_id": product_id,
            "product_name": product_name,
            "category_id": category,
            "stock_amount": stock_amount,
            "price": price,
            "image":image
           
        }

        new_pro = Products()
        new_pro.insert_new_product(**new_product)
        return make_response(jsonify({"message": "Product saved successfully"}), 201) #Created


class ViewSingleProduct(Resource):
    @jwt_required
    def get(self, product_id):
        """Fetch single product."""
        single_product = [
            product for product in get_all_products() if product['product_id'] == product_id]
        if not single_product:
            return make_response(jsonify({"message": "Product Not Found"}), 400) #Bad Request
        return make_response(jsonify({"message": single_product}), 200)  # ok

    @jwt_required
    @admin_required
    def put(self, product_id):
        """Update product."""
        data = request.get_json(force=True)
        product_name = (data["product_name"]).lower()
        category_id = data["category_id"]
        stock_amount = data["stock_amount"]
        price = data['price']

        product = [
            product for product in get_all_products() if product['product_id'] == product_id]
        if not product:
            return make_response(jsonify({'message': "Product Not found"}),  400) #Bad Request
        new_pro = Products()
        new_pro.update_product(
            product_id,
            product_name,
            category_id,
            stock_amount,
            price)
        return make_response(jsonify(
            {'message': "Updated Successfuly"}), 200)#Ok

    @jwt_required
    @admin_required
    def delete(self, product_id):
        """Delete product."""
        product = [
            product for product in get_all_products() if product['product_id'] == product_id]
        if not product:
            return make_response(jsonify({'message': "Product Not found"}),  400) #Bad Request
        new_pro = Products()
        new_pro.delete_product(product_id)
        return make_response(jsonify({'message': "Deleted Successfuly"}), 200)#ok
