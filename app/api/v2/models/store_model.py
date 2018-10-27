#app/api/v2/models/store_model.py
from ....store_database import conn_db
from flask import request,json

''' Model file that interacts with the database'''
class Products():
    def __init__(self):
        self.db = conn_db()

    def get_all_products(self):
        conn = self.db
        curr = conn.cursor()
        query = """SELECT * FROM products;"""
        curr.execute(query)
        data = curr.fetchall()
        all_products = []
        for k, v in enumerate(data):
            product_id, product_name, category_id, stock_amount, price, low_inventory_stock = v
            new_product = {"product_id": product_id,
                           "product_name": product_name,
                           "category_id": category_id,
                           "stock_amount": stock_amount,
                           "price": price,
                           "low_inventory_stock": low_inventory_stock}
            all_products.append(new_product)

        return all_products

    """Insert New Product."""

    def insert_new_product(self,  product_id, product_name, category_id, stock_amount, price, low_inventory_stock):
        database = self.db
        curr = database.cursor()
        query = "INSERT INTO products (product_id,product_name,category_id,stock_amount,price,low_inventory_stock) VALUES (%s,%s,%s,%s,%s,%s);"
        curr.execute(query, (product_id, product_name, category_id,
                             stock_amount, price, low_inventory_stock))
        database.commit()
        return {"Message": "Product added successfully"}, 201
    
    
    """Update Product."""
    def update_product(self,product_id,product_name, category_id,stock_amount, price, low_inventory_stock,):
        database = self.db
        curr = database.cursor()
        query = "UPDATE products SET product_name=%s,category_id=%s,stock_amount=%s,price=%s,low_inventory_stock=%s WHERE product_id=%s;"
        curr.execute(query, (product_name, category_id,
                             stock_amount, price, low_inventory_stock,product_id))
        database.commit()
        return {"Message": "Product Updated successfully"}, 201
    
    """Delete Product."""
    def delete_product(self,product_id):
        database = self.db
        curr = database.cursor()
        query = "DELETE FROM products WHERE product_id=%s;"
        curr.execute(query, (product_id))
        database.commit()
        return {"Message": "Product Updated successfully"}, 201
    
