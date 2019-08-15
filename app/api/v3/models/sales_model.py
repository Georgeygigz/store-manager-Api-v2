from .databases import db


class Sales(db.Model):

    __tablename__ = 'sales'

    sale_id = db.Column(db.Integer, primary_key=True)
    attendant_name = db.Column(db.String(64), index=True)
    customer_name = db.Column(db.String(100), index=True)
    product_name = db.Column(db.String(100), index=True)
    product_price = db.Column(db.Float, index=True)
    quantity =  db.Column(db.Integer, index=True)
    total_price =  db.Column(db.Float, index=True)
    date_sold =  db.Column(db.DateTime, index=True)


    def __init__(self, attendant_name, customer_name, product_name, product_price,quantity,total_price,date_sold):
        self.attendant_name = attendant_name
        self.customer_name = customer_name
        self.product_name = product_name
        self.product_price=product_price
        self.quantity = quantity
        self.total_price = total_price
        self.date_sold = date_sold


    def __repr__(self):
        return '<sale_id {}>'.format(self.sale_id)
