from . import db

class Category(db.Model):
    __tablename__ = 'categories'

    Category_ID = db.Column(db.Integer, primary_key=True)
    Category_Image = db.Column(db.String(512))
    Category_Name = db.Column(db.String(255), nullable=False)
    sort_order = db.Column(db.Integer)
