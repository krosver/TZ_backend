from . import db

class Color(db.Model):
    __tablename__ = 'colors'

    Color_ID = db.Column(db.Integer, primary_key=True)
    Color_Code = db.Column(db.String(7))
    Color_Name = db.Column(db.String(100))    
    Color_image = db.Column(db.String(512))
    Product_ID = db.Column(db.Integer, db.ForeignKey('products.Product_ID'))
    discount = db.Column(db.Integer)
    json_data = db.Column(db.JSON)
    sort_order = db.Column(db.Integer)
