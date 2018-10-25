#app/api/v2/models/store_model.py
from ....store_database import conn_db

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