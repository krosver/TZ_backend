from . import db

class Parameter(db.Model):
    __tablename__ = 'parameters'

    Parameter_ID = db.Column(db.Integer, primary_key=True)
    Product_ID = db.Column(db.Integer, db.ForeignKey('products.Product_ID'))
    chosen = db.Column(db.Boolean)
    disabled = db.Column(db.Boolean)
    extra_field_color = db.Column(db.String(100))
    extra_field_image = db.Column(db.String(512))
    name = db.Column(db.String(255))
    old_price = db.Column(db.Float)
    parameter_string = db.Column(db.String(255))
    price = db.Column(db.Float)
    sort_order = db.Column(db.Integer)
