# app/api/v1/views/category_view.py

"""This is where category API Endpoints will be captured."""
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

products = Products().get_all_products()

def view_all_categories():
    categories = Categories().get_all_categories()
    return categories

def get_user_data():
    data = request.get_json(force=True)
    return data


class ProductCategories(Resource):
    @jwt_required
    @admin_required
    def get(self):
        view_all_categories()
        """Get all products' Categories."""
        if not view_all_categories():
            return make_response(
                jsonify({"message": "No Available products categories"}), 200)#ok
        return {"message": view_all_categories()}, 200  # ok

    @jwt_required
    @admin_required
    def post(self):
        """Add a new product category."""
        all_categories = Categories().get_all_categories()
        
        category_id = len(all_categories) + 1
        category_name = get_user_data()["category_name"]

        if request.json['category_name'] in [category['category_name']
                                            for category in all_categories]:
            return make_response(jsonify(
                {"message": " {} Category Exist".format(request.json['category_name'])}))
        new_category = {
            "category_id": category_id,
            "category_name": category_name,
        }
        new_cat = Categories()
        new_cat.insert_new_produc_category(**new_category)

        return make_response(jsonify({"message": "Category added successfuly"}),201) #Created


class SingleProductCategory(Resource):
    @jwt_required
    @admin_required
    def put(self, category_id):
        """Update product category."""
        category = (get_user_data()["category_name"]).lower()
        product_category = [
            category for category in view_all_categories() if category['category_id'] == category_id]
        if not product_category:
            return make_response(jsonify({'message': "Category Not found"}), 400) #Bad Request
        new_category = Categories()
        new_category.update_product_category(category_id, category)
        return make_response(jsonify({'message': "Updated Successfuly"}), 200)

    @jwt_required
    @admin_required
    def delete(self, category_id):
        """Delete product category."""
        products = Products().get_all_products()
        product_category = [
            category for category in view_all_categories() if category['category_id'] == category_id]
        if not product_category:
            return make_response(jsonify({'message': "Category Not found"}),  400) #Bad Request
        single_product=[product for product in products if product['category_id']==category_id]
        print(single_product)
        if single_product:                 
            return make_response(jsonify(
                {"message": " {} Category is in use".format(product_category[0]['category_name'])}))
        new_category = Categories()
        new_category.delete_product_category(category_id)
        return make_response(jsonify({'message': "Deleted Successfuly"}), 200) #ok
