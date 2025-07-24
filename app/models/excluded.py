from . import db

class Excluded(db.Model):
    __tablename__ = 'excluded'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.Product_ID'))
    parameter_id = db.Column(db.Integer)
    color_id = db.Column(db.Integer)
