# app/api/v2/models/sales_model.py
from ....store_database import conn_db

class Sales:
    """Sales Records."""
    def __init__(self):
        self.db = conn_db()
        self.curr = self.db.cursor()

    def get_all_sales(self):
        """Get all sales records."""
        query = """SELECT * FROM sales;"""
        self.curr.execute(query)
        data = self.curr.fetchall()
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

    def insert_new_sale(
            self,
            sale_id,
            attedant_name,
            customer_name,
            product_name,
            product_price,
            quantity,
            total_price,
            date_sold):
        """Make a new sale Record."""
        query = "INSERT INTO sales (sale_id,attedant_name,customer_name,product_name,product_price,quantity,total_price,date_sold) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
        self.curr.execute(
            query,
            (sale_id,
             attedant_name,
             customer_name,
             product_name,
             product_price,
             quantity,
             total_price,
             date_sold))
        self.db.commit()
        return {"Message": "Sale record Save succefully"}

    def delete_sale_record(self, sale_id):
        """Delete sales."""
        query = "DELETE FROM sales WHERE sale_id=%s;"
        self.curr.execute(query, (sale_id,))
        self.db.commit()
        return {"Message": "Product Updated successfully"}
    
