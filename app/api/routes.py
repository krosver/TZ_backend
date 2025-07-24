from flask import Blueprint, jsonify
from app.extensions import db
from app.models import Product, Category

api_bp = Blueprint('api', __name__)

@api_bp.route('/info', methods=['GET'])
def get_info():
    product_count = db.session.query(Product).count()
    categories = db.session.query(Category.Category_Name).all()
    category_names = [c[0] for c in categories]

    return jsonify({
        "product_count": product_count,
        "categories": category_names
    })
