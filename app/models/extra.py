from . import db

class Extra(db.Model):
    __tablename__ = 'extras'

    Product_Extra_ID = db.Column(db.Integer, primary_key=True)
    Product_ID = db.Column(db.Integer, db.ForeignKey('products.Product_ID'))
    Characteristics = db.Column(db.Text)
    Delivery = db.Column(db.Text)
    Kit = db.Column(db.Text)
    Offer = db.Column(db.Text)
