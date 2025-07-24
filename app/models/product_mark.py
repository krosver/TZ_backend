from . import db

class ProductMark(db.Model):
    __tablename__ = 'product_marks_mapping'

    id = db.Column(db.Integer, primary_key=True)
    Product_ID = db.Column(db.Integer, db.ForeignKey('products.Product_ID'))
    Mark_ID = db.Column(db.Integer, db.ForeignKey('product_marks.Mark_ID'))
