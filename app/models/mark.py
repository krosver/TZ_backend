from . import db

class Mark(db.Model):
    __tablename__ = 'product_marks'

    Mark_ID = db.Column(db.Integer, primary_key=True)
    Mark_Name = db.Column(db.String(100), nullable=False)
