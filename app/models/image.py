from . import db

class Image(db.Model):
    __tablename__ = 'images'

    Image_ID = db.Column(db.Integer, primary_key=True)
    Image_URL = db.Column(db.String(512))
    MainImage = db.Column(db.Boolean)
    Product_ID = db.Column(db.Integer, db.ForeignKey('products.Product_ID'))
    position = db.Column(db.String(100))
    sort_order = db.Column(db.Integer)
    title = db.Column(db.String(255))
