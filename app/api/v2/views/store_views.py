# app/api/v1/views/store_views.py

"""This is where all API Endpoints will be captured."""
from flask import request, jsonify, make_response
from datetime import date
from flask_restful import Resource
from flask_jwt_extended import (jwt_required, get_jwt_identity)

# local imports
from app.api.v2.models.store_model import (Products, Sales, Categories,Users)
from app.api.v2.utils.authorization import (
    admin_required, store_attendant_required)

products = Products().get_all_products()


class ViewProducts(Resource):
    @jwt_required
    def get(self):
        """Get all products."""
        products = Products().get_all_products()
        if not products:
            return make_response(
                jsonify({"message": "No Available products"}), 200) #Ok
        return make_response(jsonify({"message": products}), 200) #Ok

    @jwt_required
    @admin_required
    def post(self):
        """Add a new product."""
        products = Products().get_all_products()
        data = request.get_json(force=True)
        product_id = len(products) + 1
        product_name = data["product_name"]
        category = data["category_id"]
        stock_amount = data["stock_amount"]
        price = data['price']
        image=data['image']

        product = [product for product in products if product['product_name']
                   == request.json['product_name']]

        if (not request.json or "product_name" not in request.json):
            return make_response(jsonify({'message': "Request Not found"}), 404)# Not Found

        if type(request.json['stock_amount'])not in [int, float]:
            return make_response(
                jsonify({"message": "Require int or float type"}))

        if request.json['product_name'] in [
                n_product['product_name'] for n_product in products]:
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
        products = Products().get_all_products()
        single_product = [
            product for product in products if product['product_id'] == product_id]
        if not single_product:
            return make_response(jsonify({"message": "Product Not Found"}), 400) #Bad Request
        return make_response(jsonify({"message": single_product}), 200)  # ok

    @jwt_required
    @admin_required
    def put(self, product_id):
        """Update product."""
        products = Products().get_all_products()
        data = request.get_json(force=True)
        product_name = (data["product_name"]).lower()
        category_id = data["category_id"]
        stock_amount = data["stock_amount"]
        price = data['price']
    
        

        product = [
            product for product in products if product['product_id'] == product_id]
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
        products = Products().get_all_products()
        product = [
            product for product in products if product['product_id'] == product_id]
        if not product:
            return make_response(jsonify({'message': "Product Not found"}),  400) #Bad Request
        new_pro = Products()
        new_pro.delete_product(product_id)
        return make_response(jsonify({'message': "Deleted Successfuly"}), 200)#ok


class ViewSalesRecord(Resource):

    @jwt_required
    def get(self):
        sales_record = Sales().get_all_sales()
        """Get all sales' records."""
        if not sales_record:
            return make_response(
                jsonify({"message": "No Available sales records"}), 200)#Ok
        return {"message": sales_record}, 200  # ok

    @jwt_required
    @store_attendant_required
    def post(self):
        """ Make a new sale record."""
        users= Users().get_all_users()
        cur_user=[user for user in users if user['email']==get_jwt_identity()]
        user_name=cur_user[0]['username']
        sales_record = Sales().get_all_sales()
        products = Products().get_all_products()
        current_date = str(date.today())
        data = request.get_json(force=True)
        current_product = [
            product for product in products if product['product_name'] == request.json['product_name']]
        if not current_product or current_product[0]['stock_amount'] == 0:
            return {
                "message": "{} Out of stock".format(
                    request.json['product_name'])}, 200 #ok
        if request.json['quantity'] > current_product[0]['stock_amount']:
            return {"message": "Quantity exeed amount in stock"}, 200 #ok

        sale_id = len(sales_record) + 1
        attedant_name = user_name
        customer_name = (data["customer_name"]).lower()
        product_name = (data["product_name"]).lower()
        price = current_product[0]['price']
        quantity = data["quantity"]
        total_price = price * quantity
        date_sold = current_date

        if (not request.json or "product_name" not in request.json):
            return {'message': "Request Not found"},  400 #Bad Request

        if request.json['product_name'] in [sale['product_name']
                                            for sale in sales_record]:
            return {
                "message": "{} Exist in cart".format(
                    request.json['product_name'])}, 200 #ok

        new_sale = {
            "sale_id": sale_id,
            "attedant_name": attedant_name,
            "customer_name": customer_name,
            "product_name": product_name,
            "product_price": price,
            "quantity": quantity,
            "total_price": total_price,
            "date_sold": date_sold
        }
        current_product[0]['stock_amount'] -= request.json['quantity']
        update_product = Products()
        update_product.update_stock_amount(
            current_product[0]['product_name'],
            current_product[0]['stock_amount'])
        new_sales_record = Sales()
        new_sales_record.insert_new_sale(**new_sale)
        return {"message": "Item added successfuly"}, 201  # created


class SingleSale(Resource):
    @jwt_required
    def get(self, sale_id):
        """ Get single sale record."""
        sales_record = Sales().get_all_sales()
        single_sale = [
            sale for sale in sales_record if sale['sale_id'] == sale_id]
        if single_sale:
            return {"message": single_sale}, 200  # ok
        return {"message": "Sale Not Found"},   400 #Bad Request

    @jwt_required
    def delete(self,sale_id):
        """Delete from cart."""
        sales_record = Sales().get_all_sales()
        single_sale = [
            sale for sale in sales_record if sale['sale_id'] == sale_id]
        if not single_sale:
            return make_response(jsonify({'message': "Sale Not found"}),  400) #Bad Request
        sale_record = Sales()
        sale_record.delete_sale_record(sale_id)
        return make_response(jsonify({'message': "Deleted Successfuly"}), 200) #ok

class SingleAttedantSales(Resource):
    @jwt_required
    def get(self,attedant_name):
        """ Get single sale record for specific user."""
        sales_record = Sales().get_all_sales()
        single_sale = [
            sale for sale in sales_record if sale['attedant_name'] == attedant_name]
        if single_sale:
            return {"message": single_sale}, 200  # ok
        return {"message": "Sale Not Found"},   400 #Bad Request        


class ProductCategories(Resource):
    @jwt_required
    @admin_required
    def get(self):
        categories = Categories().get_all_categories()
        """Get all products' Categories."""
        if not categories:
            return make_response(
                jsonify({"message": "No Available products categories"}), 200)#ok
        return {"message": categories}, 200  # ok

    @jwt_required
    @admin_required
    def post(self):
        """Add a new product category."""
        all_categories = Categories().get_all_categories()
        data = request.get_json(force=True)
        category_id = len(all_categories) + 1
        category_name = data["category_name"]
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
        categories = Categories().get_all_categories()
        data = request.get_json(force=True)
        category_name = (data["category_name"]).lower()

        product_category = [
            category for category in categories if category['category_id'] == category_id]
        if not product_category:
            return make_response(jsonify({'message': "Category Not found"}), 400) #Bad Request
        new_category = Categories()
        new_category.update_product_category(category_id, category_name)
        return make_response(jsonify({'message': "Updated Successfuly"}), 200)

    @jwt_required
    @admin_required
    def delete(self, category_id):
        """Delete product category."""
        products = Products().get_all_products()
        categories = Categories().get_all_categories()
        product_category = [
            category for category in categories if category['category_id'] == category_id]
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
