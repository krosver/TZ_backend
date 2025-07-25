from . import db

class Product(db.Model):
    __tablename__ = 'products'

    Product_ID = db.Column(db.Integer, primary_key=True)
    Created_At = db.Column(db.DateTime)
    OnMain = db.Column(db.Boolean)
    Product_Name = db.Column(db.String(255), nullable=False)
    Updated_At = db.Column(db.DateTime)
    importance_num = db.Column(db.JSON)
    moysklad_connector_products_data = db.Column(db.JSON)
    tags = db.Column(db.JSON)
