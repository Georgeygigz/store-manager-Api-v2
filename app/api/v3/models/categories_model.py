from .databases import db


class Categories(db.Model):

    __tablename__ = 'categories'

    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(64), index=True)

    def __init__(self, category_name):
        self.category_name = category_name

    def __repr__(self):
        return '<category_id {}>'.format(self.category_id)
