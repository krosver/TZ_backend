from . import db

class ReviewVideo(db.Model):
    __tablename__ = 'reviews_video'

    Video_ID = db.Column(db.Integer, primary_key=True)
    Product_ID = db.Column(db.Integer, db.ForeignKey('products.Product_ID'))
    Poster_URL = db.Column(db.String(512))
    Video_URL = db.Column(db.String(512))
    sort_order = db.Column(db.Integer)
