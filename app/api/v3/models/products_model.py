from .databases import db


class Products(db.Model):

    __tablename__ = 'products'

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(64), index=True)
    category_id = db.Column(db.Integer, index=True)
    stock_amount = db.Column(db.Integer, index=True)
    price = db.Column(db.Float, index=True)
    low_inventory_stock =  db.Column(db.Integer, index=True)

    def __init__(self,product_id, product_name, category_id, stock_amount, price,low_inventory_stock):
        self.product_id = product_id
        self.product_name = product_name
        self.category_id = category_id
        self.stock_amount = stock_amount
        self.price = price
        self.low_inventory_stock = low_inventory_stock

    def __repr__(self):
        return '<product_id {}>'.format(self.product_id)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    def update_(self, **kwargs):
        """
        update entries
        """
        for field, value in kwargs.items():
            setattr(self, field, value)
        db.session.commit()
    
    def delete_(self,product):
        db.session.delete(product)
        db.session.commit()
        return self