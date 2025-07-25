from . import db

class Review(db.Model):
    __tablename__ = 'reviews'

    Photo_ID = db.Column(db.Integer, primary_key=True)
    Product_ID = db.Column(db.Integer, db.ForeignKey('products.Product_ID'))
    Photo_URL = db.Column(db.String(512))
    sort_order = db.Column(db.Integer)
