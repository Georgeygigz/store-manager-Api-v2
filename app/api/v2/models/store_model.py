#app/api/v2/models/store_model.py
from ....store_database import conn_db


"""Model file that interacts with the database."""

class DbInitializer:
    def __init__(self):
        self.db = conn_db()

    def init_db(self):
        conn = self.db
        return conn
    
    def init_cursor(self):
        conn = self.init_db()
        cursor = conn.cursor()
        return cursor
    
    


class Products(DbInitializer):

    def get_all_products(self):
        """Get all products."""
        try:
            curr = self.init_db().cursor()
            query = """SELECT * FROM products;"""
            curr.execute(query)
            data = curr.fetchall()
            all_products = []
            for k, v in enumerate(data):
                product_id, product_name, category_id, stock_amount, price, low_inventory_stock = v
                new_product = {"product_id": product_id,
                               "product_name": product_name,
                               "category_id": int(category_id),
                               "stock_amount": stock_amount,
                               "price": price,
                               "low_inventory_stock": low_inventory_stock}
                all_products.append(new_product)
            return all_products

        except Exception as e:
            return {"Message": e}

    def insert_new_product(self, *args):
        """Insert New Product."""
        database = self.init_db()
        product_id, product_name, category_id, stock_amount, price, low_inventory_stock = args
        try:
            curr = database.cursor()
            query = "INSERT INTO products (product_id,product_name,category_id,stock_amount,price,low_inventory_stock) VALUES (%s,%s,%s,%s,%s,%s);"
            curr.execute(query, (product_id, product_name, category_id,
                                 stock_amount, price, low_inventory_stock))
            database.commit()
            return {"Message": "Product added successfully"}
        except Exception as e:
            return {"Message": e}

    def update_product(self, *args):
        """Update Product."""
        database = self.init_db()
        product_id, product_name, category_id, stock_amount, price, low_inventory_stock = args
        try:
            curr = database.cursor()
            query = "UPDATE products SET product_name=%s,category_id=%s,stock_amount=%s,price=%s,low_inventory_stock=%s WHERE product_id=%s;"
            curr.execute(
                query,
                (product_name,
                 category_id,
                 stock_amount,
                 price,
                 low_inventory_stock,
                 product_id))
            database.commit()
            return {"Message": "Product Updated successfully"}
        except Exception as e:
            return {"Message": e}

    def update_stock_amount(self, product_name, stock_amount):
        """Update Product."""
        database = self.init_db()
        try:
            curr = database.cursor()
            query = "UPDATE products SET stock_amount=%s WHERE product_name=%s;"
            curr.execute(query, (stock_amount, product_name))
            database.commit()
            curr.close()
            return {"Message": "Product Updated successfully"}
        except Exception as e:
            return {"Message": e}

    def delete_product(self, product_id):
        """Delete Product."""
        database = self.init_db()
        try:
            curr = database.cursor()
            query = "DELETE FROM products WHERE product_id=%s;"
            curr.execute(query, (product_id,))
            database.commit()
            return {"Message": "Product Updated successfully"}

        except Exception as e:
            return {"Message": e}


class Sales(DbInitializer):
    """Sales Records."""

    def get_all_sales(self):
        """Get all sales records."""
        conn = self.init_db()
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
                    "date_sold": str(date_sold)
                }
                all_sale_records.append(new_sale)

            return all_sale_records
        except Exception as e:
            return {"Message": e}

    def insert_new_sale(self, *args):
        """Make a new sale Record."""
        database = self.init_db()
        sale_id, attedant_name, customer_name, product_name, product_price, quantity, total_price, date_sold = args
        curr = database.cursor()
        query = "INSERT INTO sales (sale_id,attedant_name,customer_name,product_name,product_price,quantity,total_price,date_sold) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
        curr.execute(
            query,
            (sale_id,
             attedant_name,
             customer_name,
             product_name,
             product_price,
             quantity,
             total_price,
             date_sold))
        database.commit()
        return {"Message": "Sale record Save succefully"}


class Categories(DbInitializer):
    def __init__(self):
        """Products' category."""

    def get_all_categories(self):
        """Get all products' categories"""
        conn = self.init_db()
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
        database = self.init_db()
        curr = database.cursor()
        query = "INSERT INTO products_category (category_id,category_name) VALUES (%s,%s);"
        curr.execute(query, (category_id, category_name))
        database.commit()
        return {"Message": "Sale record Save succefully"}

    def update_product_category(self, category_id, category_name):
        """Update product category."""
        database = self.init_db()
        try:
            curr = database.cursor()
            query = "UPDATE products_category SET category_name=%s WHERE category_id=%s;"
            curr.execute(query, (category_name, category_id))
            database.commit()
            return {"Message": "Category Updated successfully"}
        except Exception as e:
            return {"Message": e}

    def delete_product_category(self, category_id):
        """Delete Category."""
        database = self.init_db()
        try:
            curr = database.cursor()
            query = "DELETE FROM products_category WHERE category_id=%s;"
            curr.execute(query, (category_id,))
            database.commit()
            return {"Message": "Product Updated successfully"}

        except Exception as e:
            return {"Message": e}


class Users(DbInitializer):
    """Users mode."""

    def insert_new_user(self, *args):
        """Insert new user."""
        database = self.init_db()
        curr = self.init_cursor()
        user_id, username, email, password, role = args
        query = "INSERT INTO users (user_id, username,email, password,user_type) VALUES (%s,%s,%s,%s,%s);"
        curr.execute(query, (user_id, username, email, password, role))
        # import pdb; pdb.set_trace()

        database.commit()
        curr.close()
        return {"Message": "User created succefully"}

    def get_all_users(self):
        """Get all users."""
        conn = self.init_db()
        curr = self.init_cursor()
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

    def update_user(self, user_id, role):
        """Update product category."""
        database =  self.init_db()
        try:
            curr = self.init_cursor()
            query = "UPDATE users SET user_type=%s WHERE user_id=%s;"
            curr.execute(query, (role, user_id))
            database.commit()
            return {"Message": "Category Updated successfully"}
        except Exception as e:
            return {"Message": e}


