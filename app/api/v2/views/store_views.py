# app/api/v1/views/store_views.py

"""This is where all API Endpoints will be captured."""
from flask import request, jsonify, make_response
from datetime import date
from flask_restful import Resource

# local imports
from app.api.v2.models.store_model import (Products,Sales,Categories)
from app.api.v2.utils.utils import Validate



products = Products().get_all_products()
sales_record=Sales().get_all_sales()
categories=Categories().get_all_categories()

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
            return make_response(jsonify({'Error': "Request Not found"}), 404)  # not found

        if type((request.json['stock_amount']) or (request.json['price'])) not in [int, float]:
            return make_response(jsonify({"Error": "Require int or float type"}))

        if request.json['product_name'] in [n_product['product_name'] for n_product in products]:
            product[0]["stock_amount"] += request.json['stock_amount']
            return make_response(jsonify({"Products": product}), 200)  # ok

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

        return make_response(jsonify({"New Product": new_product}), 201)  # created

class ViewSingleProduct(Resource):
    """Fetch single product."""
    def get(self,product_id):
        single_product = [
            product for product in products if product['product_id'] == product_id]
        if not single_product:
            return make_response(jsonify({"Error": "Product Not Found"}), 404)  # Not found
        return make_response(jsonify({"Product": single_product}), 200)  # ok
    

    def put(self,product_id): 
        """Update product."""
        data = request.get_json(force=True)
        product_name = data["product_name"]
        category_id = data["category_id"]
        stock_amount = data["stock_amount"]
        price = data['price']
        low_inventory_stock = data['low_inventory_stock']
        product=[product for product in products if product['product_id']==product_id]
        if not product:
            return make_response(jsonify({'Error':"Product Not found"}), 400)
        new_pro=Products()
        new_pro.update_product(product_id,product_name,category_id,stock_amount,price,low_inventory_stock)
     
        return make_response(jsonify({'Message':"{} Updated Successfuly".format(product[0]['product_name'])}), 200) #ok
    
    def delete(self,product_id): 
        """Delete product."""
        product=[product for product in products if product['product_id']==product_id]
        if not product:
            return make_response(jsonify({'Error':"Product Not found"}), 400)
        new_pro=Products()
        new_pro.delete_product(product_id)
        return make_response(jsonify({'Message':"Deleted Successfuly"}), 200) #ok

class ViewSalesRecord(Resource):
    """Get all sales' records."""
    def get(self):
        if not sales_record:
            return make_response(jsonify({"Message": "No Available sales records"}), 200)
        return {"Sales Record": sales_record}, 200  # ok
    """ Make a new sale record."""
    def post(self):
        current_date = str(date.today())
        data = request.get_json(force=True)
        #Validate().validate_empty_sales_inputs(data)
        current_product = [
            product for product in products if product['product_name'] == request.json['product_name']]
        if not current_product or current_product[0]['stock_amount'] == 0:
            return {"Message": "{} Out of stock, Please add {} in stock beforemaking a sale".format(request.json['product_name'], request.json['product_name'])}, 200
        sale_id = len(sales_record)+1
        attedant_name = data["attedant_name"]
        customer_name = data["customer_name"]
        product_name = data["product_name"]
        price = current_product[0]['price']
        quantity = data["quantity"]
        total_price = price*quantity
        date_sold = current_date

        if (not request.json or not "product_name" in request.json):
            return {'Error': "Request Not found"}, 400  # not found

        if request.json['product_name'] in [sale['product_name'] for sale in sales_record]:
            # ok
            return {"Message": "{} Exist in cart".format(request.json['product_name'])}, 200

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
        new_sales_record=Sales()
        new_sales_record.insert_new_sale(**new_sale)
        current_product[0]['stock_amount'] -= request.json['quantity']
        return {"New Sale Record": new_sale}, 201  # created
 
class SingleSale(Resource):
    """ Get single sale record."""
    def get(self,sale_id):
        single_sale = [
            sale for sale in sales_record if sale['sale_id'] == sale_id]
        if single_sale:
            return {"Sale": single_sale}, 200  # ok
        return {"Message": "Sale Not Found"}, 400  # ok

class ProductCategories(Resource):
    """Get all products' Categories."""
    def get(self):
        if not categories:
            return make_response(jsonify({"Message": "No Available products categories"}), 200)
        return {"Sales Record": categories}, 200  # ok
    
    """Add a new product category."""
    def post(self):
        data = request.get_json(force=True) 
        category_id = len(categories)+1
        category_name = data["category_name"]
        category=[c for c in categories if c['category_name']==request.json['category_name']]
        if category:
            return make_response(jsonify({"Message":" {} Category Exist".format(request.json['category_name'])}))
        new_category = {
            "category_id": category_id,
            "category_name": category_name,
        }
        new_cat=Categories()
        new_cat.insert_new_produc_category(**new_category)
        
        return make_response(jsonify({"Category":new_category}))

class SinleProductCategory(Resource):
    def put(self,category_id): 
        """Update product."""
        data = request.get_json(force=True)
        category_name = data["category_name"]
   
        product_category=[category for category in categories if category['category_id']==category_id]
        if not product_category:
            return make_response(jsonify({'Error':"Category Not found"}), 400)
        new_category=Categories()
        new_category.update_product_category(category_id,category_name)
    
        return make_response(jsonify({'Message':"{} Updated Successfuly".format(product_category[0]['category_name'])}), 200) #ok
    
    def delete(self,category_id):
        """Delete product."""
        product_category=[category for category in categories if category['category_id']==category_id]
        if not product_category:
            return make_response(jsonify({'Error':"Category Not found"}), 400)
        new_category=Categories()
        new_category.delete_product_category(category_id)
    
        return make_response(jsonify({'Message':"{} Deleted Successfuly".format(product_category[0]['category_name'])}), 200) #ok

