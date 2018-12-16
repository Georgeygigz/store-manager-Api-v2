# app/api/v1/views/sales_view.py

"""This is where sales API Endpoints will be captured."""
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

def get_all_sales():
    sales_record = Sales().get_all_sales()
    return sales_record

def check_empty_inputs():
    empty_data = [request.json['customer_name'],request.json['product_name'],request.json['quantity']]
    for empty_input in empty_data:
        if (empty_input ==""):
            return True

def check_exist_in_cart():    
    if request.json['product_name'] in [sale['product_name']
                                        for sale in get_all_sales()]:
        return True

products = Products().get_all_products()

class SingleSale(Resource):
    @jwt_required
    def get(self, sale_id):
        """ Get single sale record."""
        single_sale = [
            sale for sale in get_all_sales() if sale['sale_id'] == sale_id]
        if single_sale:
            return {"message": single_sale}, 200  # ok
        return {"message": "Sale Not Found"},   400 #Bad Request

    @jwt_required
    def delete(self,sale_id):
        """Delete from cart."""
        single_sale_record = [
            sale_record for sale_record in get_all_sales() if sale_record['sale_id'] == sale_id]
        if not single_sale_record:
            return make_response(jsonify({'message': "Sale Not found"}),  400) #Bad Request
        sale_record = Sales()
        sale_record.delete_sale_record(sale_id)
        return make_response(jsonify({'message': "Deleted Successfuly"}), 200) #ok

class SingleAttedantSales(Resource):
    @jwt_required
    def get(self,attedant_name):
        """ Get single sale record for specific user."""
        sale_record = [
            single_sale for single_sale in get_all_sales() if single_sale['attedant_name'] == attedant_name]
        if sale_record:
            return {"message": sale_record}, 200  # ok
        return {"message": "Sale Not Found"},   400 #Bad Request        



class ViewSalesRecord(Resource):
    @jwt_required
    def get(self):
        """Get all sales' records."""
        if not get_all_sales():
            return make_response(
                jsonify({"message": "No Available sales records"}), 200)#Ok
        return {"message": get_all_sales()}, 200  # ok

    @jwt_required
    @store_attendant_required
    def post(self):
        """ Make a new sale record."""
        cur_user=[user for user in Users().get_all_users() if user['email']==get_jwt_identity()]
        products = Products().get_all_products()
        data = request.get_json(force=True)
        required_inputs = ['customer_name', 'product_name','quantity']
        inputs=[field for field in required_inputs if field not in request.json ]
        if inputs:
            return make_response(jsonify({'message': " {} is required".format(inputs[0])}))

        if check_empty_inputs():
            return make_response(jsonify({'message': "All fields are required"}))

        current_product = [
            product for product in products if product['product_name'] == request.json['product_name']]
        if not current_product or current_product[0]['stock_amount'] == 0:
            return {
                "message": "{} Out of stock".format(
                    request.json['product_name'])}, 200 #ok
        if request.json['quantity'] > current_product[0]['stock_amount']:
            return {"message": "Quantity exeed amount in stock"}, 200 #ok

        sale_id = len(get_all_sales()) + 1
        attedant_name = cur_user[0]['username']
        customer_name = (data["customer_name"]).lower()
        product_name = (data["product_name"]).lower()
        price = current_product[0]['price']
        quantity = data["quantity"]
        total_price = price * quantity
        date_sold = str(date.today())

        if check_exist_in_cart():
            return {"message": "{} Exist in cart".format(
                    request.json['product_name'])}, 200 #ok

        new_sale = {"sale_id": sale_id, "attedant_name": attedant_name,"customer_name": customer_name, 
                    "product_name": product_name, "product_price": price, "quantity": quantity,
                    "total_price": total_price, "date_sold": date_sold
        }
        current_product[0]['stock_amount'] -= request.json['quantity']
        update_product = Products().update_stock_amount(
            current_product[0]['product_name'],
            current_product[0]['stock_amount'])
        new_sales_record = Sales().insert_new_sale(**new_sale)
        return {"message": "Item added successfuly"}, 201  # created