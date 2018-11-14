# app/api/v2/models/products_model.py
from ....store_database import conn_db

"""Model file that interacts with the database."""
class Products():
    def __init__(self):
        self.db = conn_db()

    def get_all_products(self):
        """Get all products."""
        conn = self.db
        try:
            curr = conn.cursor()
            query = """SELECT * FROM products order by product_id;"""
            curr.execute(query)
            data = curr.fetchall()
            all_products = []
            for k, v in enumerate(data):
                product_id, product_name, category_id, stock_amount, price,image = v
                new_product = {"product_id": product_id,
                               "product_name": product_name,
                               "category_id": int(category_id),
                               "stock_amount": stock_amount,
                               "price": price,
                               "image":image}
                all_products.append(new_product)
            return all_products

        except Exception as e:
            return {"Message": e}

    def insert_new_product(
            self,
            product_id,
            product_name,
            category_id,
            stock_amount,
            price,
            image):
        """Insert New Product."""
        database = self.db
        try:
            curr = database.cursor()
            query = "INSERT INTO products (product_id,product_name,category_id,stock_amount,price,image) VALUES (%s,%s,%s,%s,%s,%s);"
            curr.execute(query, (product_id, product_name, category_id,
                                 stock_amount, price,image))
            database.commit()
            return {"Message": "Product added successfully"}
        except Exception as e:
            return {"Message": e}

    def update_product(
        self,
        product_id,
        product_name,
        category_id,
        stock_amount,
        price
    ):
        """Update Product."""
        database = self.db
        try:
            curr = database.cursor()
            query = "UPDATE products SET product_name=%s,category_id=%s,stock_amount=%s,price=%s WHERE product_id=%s;"
            curr.execute(
                query,
                (product_name,
                 category_id,
                 stock_amount,
                 price,
                 product_id))
            database.commit()
            return {"Message": "Product Updated successfully"}
        except Exception as e:
            return {"Message": e}

    def update_stock_amount(self, product_name, stock_amount):
        """Update Product."""
        database = self.db
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
        database = self.db
        try:
            curr = database.cursor()
            query = "DELETE FROM products WHERE product_id=%s;"
            curr.execute(query, (product_id,))
            database.commit()
            return {"Message": "Product Updated successfully"}

        except Exception as e:
            return {"Message": e}


