from . import db

class ProductCategory(db.Model):
    __tablename__ = 'product_categories'

    id = db.Column(db.Integer, primary_key=True)
    Product_ID = db.Column(db.Integer, db.ForeignKey('products.Product_ID'))
    Category_ID = db.Column(db.Integer, db.ForeignKey('categories.Category_ID'))
