# app/api/v2/models/categoty_model.py
from ....store_database import conn_db

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
        return {"Message": "Sale record Save succefully"}

    def update_product_category(self, category_id, category_name):
        """Update product category."""
        database = self.db
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
        database = self.db
        try:
            curr = database.cursor()
            query = "DELETE FROM products_category WHERE category_id=%s;"
            curr.execute(query, (category_id,))
            database.commit()
            return {"Message": "Product Updated successfully"}

        except Exception as e:
            return {"Message": e}


