# app/api/v2/models/products_model.py
from ....store_database import conn_db

"""Model file that interacts with the database."""
class Products():
    def __init__(self):
        self.db = conn_db()
        self.curr = self.db.cursor()

    def get_all_products(self):
        """Get all products."""
        query = """SELECT * FROM products order by product_id;"""
        self.curr.execute(query)
        data = self.curr.fetchall()
        all_products = []
        for k,v in enumerate(data):
            product_id, product_name, category_id, stock_amount, price,image = v
            new_product = {"product_id": product_id,
                            "product_name": product_name,
                            "category_id": int(category_id),
                            "stock_amount": stock_amount,
                            "price": price,
                            "image":image}
            all_products.append(new_product)
        return all_products

    def insert_new_product(
            self,
            product_id,
            product_name,
            category_id,
            stock_amount,
            price,
            image):
        """Insert New Product."""
        query = "INSERT INTO products (product_id,product_name,category_id,stock_amount,price,image) VALUES (%s,%s,%s,%s,%s,%s);"
        self.curr.execute(query, (product_id, product_name, category_id,
                                stock_amount, price,image))
        self.db.commit()
        return {"Message": "Product added successfully"}

    def update_product(
        self,
        product_id,
        product_name,
        category_id,
        stock_amount,
        price
    ):
        """Update Product."""
        query = "UPDATE products SET product_name=%s,category_id=%s,stock_amount=%s,price=%s WHERE product_id=%s;"
        self.curr.execute(
            query,
            (product_name,
                category_id,
                stock_amount,
                price,
                product_id))
        self.db.commit()
        return {"Message": "Product Updated successfully"}

    def update_stock_amount(self, product_name, stock_amount):
        """Update Product."""
        query = "UPDATE products SET stock_amount=%s WHERE product_name=%s;"
        self.curr.execute(query, (stock_amount, product_name))
        self.db.commit()
        self.curr.close()
        return {"Message": "Product Updated successfully"}

    def delete_product(self, product_id):
        """Delete Product."""
        query = "DELETE FROM products WHERE product_id=%s;"
        self.curr.execute(query, (product_id,))
        self.db.commit()
        return {"Message": "Product Updated successfully"}


