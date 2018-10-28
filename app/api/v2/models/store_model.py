#app/api/v2/models/store_model.py
from ....store_database import conn_db


''' Model file that interacts with the database'''
class Products():
    def __init__(self):
        self.db = conn_db()

    def get_all_products(self):
        conn = self.db
        try:
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
        except Exception as e:
            print(e)

    """Insert New Product."""

    def insert_new_product(self,  product_id, product_name, category_id, stock_amount, price, low_inventory_stock):
        database = self.db
        try:
            curr = database.cursor()
            query = "INSERT INTO products (product_id,product_name,category_id,stock_amount,price,low_inventory_stock) VALUES (%s,%s,%s,%s,%s,%s);"
            curr.execute(query, (product_id, product_name, category_id,
                                stock_amount, price, low_inventory_stock))
            database.commit()
            return {"Message": "Product added successfully"}, 201
        except Exception as e:
            print(e)

    
    """Update Product."""
    def update_product(self,product_id,product_name, category_id,stock_amount, price, low_inventory_stock,):
        database = self.db
        try:
            curr = database.cursor()
            query = "UPDATE products SET product_name=%s,category_id=%s,stock_amount=%s,price=%s,low_inventory_stock=%s WHERE product_id=%s;"
            curr.execute(query, (product_name, category_id,
                                stock_amount, price, low_inventory_stock,product_id))
            database.commit()
            return {"Message": "Product Updated successfully"}, 201
        except Exception as e:
            print(e)
    
    """Delete Product."""
    def delete_product(self,product_id):
        database = self.db
        try:
            curr = database.cursor()
            query = "DELETE FROM products WHERE product_id=%s;"
            curr.execute(query, (product_id,))
            database.commit()
            return {"Message": "Product Updated successfully"}, 201

        except Exception as e:
            return {"Message": e}

class Sales:
    def __init__(self):
        self.db = conn_db()

    def get_all_sales(self):
        conn = self.db
        try:
            curr = conn.cursor()
            query = """SELECT * FROM sales;"""
            curr.execute(query)
            data = curr.fetchall()
            all_sale_records = []
            for k, v in enumerate(data):
                sale_id,attedant_name, customer_name, product_name, product_price, quantity, total_price, date_sold = v
                new_sale = {
                    "sale_id": sale_id,
                    "attedant_name": attedant_name,
                    "customer_name": customer_name,
                    "product_name": product_name,
                    "product_price": product_price,
                    "quantity": quantity,
                    "total_price": total_price,
                    "date_sold": date_sold
                }
                all_sale_records.append(new_sale)

            return all_sale_records
        except Exception as e:
            return {"Message": e}
    
    def insert_new_sale(self, sale_id,attedant_name, customer_name, product_name, product_price, quantity, total_price, date_sold):
        database = self.db
        curr = database.cursor()
        query = "INSERT INTO sales (sale_id,attedant_name,customer_name,product_name,product_price,quantity,total_price,date_sold) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
        curr.execute(query, (sale_id,attedant_name, customer_name,
                             product_name, product_price, quantity, total_price, date_sold))
        database.commit()
        return {"Message": "Sale record Save succefully"}, 201

class Categories:
    def __init__(self):
        self.db = conn_db()

    def get_all_categories(self):
        conn = self.db
        try:
            curr = conn.cursor()
            query = """SELECT * FROM products_category;"""
            curr.execute(query)
            data = curr.fetchall()
            all_categories = []
              
            for k, v in enumerate(data):
                category_id,category_name = v
                categories = {
                    "category_id": category_id,
                    "category_name": category_name,
                }
                all_categories.append(categories)

            return all_categories
        except Exception as e:
            return {"Message": e}
