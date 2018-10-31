# app/api/v2/models/store_model.py
from ....store_database import conn_db


"""Model file that interacts with the database."""
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


    def insert_new_product(self,  product_id, product_name, category_id, stock_amount, price, low_inventory_stock):
        """Insert New Product."""
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


    def update_product(self, product_id, product_name, category_id, stock_amount, price, low_inventory_stock,):
        """Update Product."""
        database = self.db
        try:
            curr = database.cursor()
            query = "UPDATE products SET product_name=%s,category_id=%s,stock_amount=%s,price=%s,low_inventory_stock=%s WHERE product_id=%s;"
            curr.execute(query, (product_name, category_id,
                                 stock_amount, price, low_inventory_stock, product_id))
            database.commit()
            return {"Message": "Product Updated successfully"}, 201
        except Exception as e:
            print(e)

    def delete_product(self, product_id):
        """Delete Product."""
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
    """Sales Records."""
    def __init__(self):
        self.db = conn_db()

    def get_all_sales(self):
        """Get all sales records."""
        conn = self.db
        try:
            curr = conn.cursor()
            query = """SELECT * FROM sales;"""
            curr.execute(query)
            data = curr.fetchall()
            all_sale_records = []
            for k, v in enumerate(data):
                sale_id, attedant_name, customer_name, product_name, product_price, quantity, total_price, date_sold = v
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
    
    
    def insert_new_sale(self, sale_id, attedant_name, customer_name, product_name, product_price, quantity, total_price, date_sold):
        """Make a new sale Record."""
        database = self.db
        curr = database.cursor()
        query = "INSERT INTO sales (sale_id,attedant_name,customer_name,product_name,product_price,quantity,total_price,date_sold) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
        curr.execute(query, (sale_id, attedant_name, customer_name,
                             product_name, product_price, quantity, total_price, date_sold))
        database.commit()
        return {"Message": "Sale record Save succefully"}, 201


class Categories:
    def __init__(self):
        """Products' category."""
        self.db = conn_db()
    
    
    def get_all_categories(self):
        """Get all products' categories"""
        conn = self.db
        try:
            curr = conn.cursor()
            query = """SELECT * FROM products_category;"""
            curr.execute(query)
            data = curr.fetchall()
            all_categories = []

            for k, v in enumerate(data):
                category_id, category_name = v
                categories = {
                    "category_id": category_id,
                    "category_name": category_name,
                }
                all_categories.append(categories)

            return all_categories
        except Exception as e:
            return {"Message": e}

   
    def insert_new_produc_category(self, category_id, category_name):
        """Add new product category."""
        database = self.db
        curr = database.cursor()
        query = "INSERT INTO products_category (category_id,category_name) VALUES (%s,%s);"
        curr.execute(query, (category_id, category_name))
        database.commit()
        return {"Message": "Sale record Save succefully"}, 201
    
    def update_product_category(self, category_id, category_name):
        """Update product category."""
        database = self.db
        try:
            curr = database.cursor()
            query = "UPDATE products_category SET category_name=%s WHERE category_id=%s;"
            curr.execute(query, (category_name, category_id))
            database.commit()
            return {"Message": "Category Updated successfully"}, 201
        except Exception as e:
            print(e)
    
    
    def delete_product_category(self, category_id):
        """Delete Category."""
        database = self.db
        try:
            curr = database.cursor()
            query = "DELETE FROM products_category WHERE category_id=%s;"
            curr.execute(query, (category_id,))
            database.commit()
            return {"Message": "Product Updated successfully"}, 201

        except Exception as e:
            return {"Message": e}

class Users:
    """Users mode."""
    def __init__(self):
        self.db = conn_db()
    
    """Insert new user."""
    def insert_new_user(self, user_id, username, email, password, role):
        database = self.db
        curr = database.cursor()
        query = "INSERT INTO users (user_id, username,email, password,user_type) VALUES (%s,%s,%s,%s,%s);"
        curr.execute(query, (user_id, username, email, password, role))
        database.commit()
        curr.close()
        return {"Message": "User created succefully"}, 201

    """Get all users."""
    def get_all_users(self):
        conn = self.db
        curr = conn.cursor()
        query = """SELECT * FROM users;"""
        curr.execute(query)
        data = curr.fetchall()
        all_users = []

        for k, v in enumerate(data):
            user_id, username, email, password, role = v
            users = {"user_id": user_id,
                     "username": username,
                     "email": email,
                     "password": password,
                     "role": role}
            all_users.append(users)
        return all_users


