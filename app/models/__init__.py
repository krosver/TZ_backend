from flask_sqlalchemy import SQLAlchemy

from app.extensions import db

from .category import Category
from .product import Product
from .product_category import ProductCategory
from .color import Color
from .parameter import Parameter
from .extra import Extra
from .image import Image
from .review import Review
from .review_video import ReviewVideo
from .mark import Mark
from .product_mark import ProductMark
from .excluded import Excluded

__all__ = [
    "Category",
    "Product",
    "ProductCategory",
    "Color",
    "Parameter",
    "Extra",
    "Image",
    "Review",
    "ReviewVideo",
    "Mark",
    "ProductMark",
    "Excluded",
    "db"
]