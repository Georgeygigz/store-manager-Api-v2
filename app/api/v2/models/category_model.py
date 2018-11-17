# app/api/v2/models/categoty_model.py
from ....store_database import conn_db

class Categories:
    def __init__(self):
        """Products' category."""
        self.db = conn_db()
        self.curr = self.db.cursor()

    def get_all_categories(self):
        """Get all products' categories"""
        query = """SELECT * FROM products_category;"""
        self.curr.execute(query)
        data = self.curr.fetchall()
        all_categories = []
        for k, v in enumerate(data):
            category_id, category_name = v
            categories = {
                "category_id": category_id,
                "category_name": category_name,
            }
            all_categories.append(categories)

        return all_categories


    def insert_new_produc_category(self, category_id, category_name):
        """Add new product category."""
        query = "INSERT INTO products_category (category_id,category_name) VALUES (%s,%s);"
        self.curr.execute(query, (category_id, category_name))
        self.db.commit()
        return {"Message": "Sale record Save succefully"}

    def update_product_category(self, category_id, category_name):
        """Update product category."""
        query = "UPDATE products_category SET category_name=%s WHERE category_id=%s;"
        self.curr.execute(query, (category_name, category_id))
        self.db.commit()
        return {"Message": "Category Updated successfully"}


    def delete_product_category(self, category_id):
        """Delete Category."""
        query = "DELETE FROM products_category WHERE category_id=%s;"
        self.curr.execute(query, (category_id,))
        self.db.commit()
        return {"Message": "Product Updated successfully"}



