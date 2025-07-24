import requests
import logging
from app.models import Category, Mark, Product, Color, Parameter, Image, Review, ReviewVideo, Extra, Excluded
from datetime import datetime
from app.database import SessionLocal

logger = logging.getLogger(__name__)

API_URLS = [
    "https://bot-igor.ru/api/products?on_main=true",
    "https://bot-igor.ru/api/products?on_main=false"
]

def parse_datetime(dt_str):
    try:
        return datetime.strptime(dt_str, "%a, %d %b %Y %H:%M:%S %Z")
    except Exception:
        return None

def add_to_bd(data):
    session = SessionLocal()
    try:
        if 'categories' in data:
            for cat in data["categories"]:
                category = Category(
                    Category_ID=cat["Category_ID"],
                    Category_Name=cat["Category_Name"],
                    Category_Image=cat["Category_Image"],
                    sort_order=cat.get("sort_order"),
                )
                session.merge(category)

        session.commit()
        
        if 'product_marks' in data:
            for product_marks in data["product_marks"]:
                mark = Mark(
                    Mark_ID=product_marks["Mark_ID"],
                    Mark_Name=product_marks["Mark_Name"],
                )
                session.merge(mark)

        session.commit()

        if 'products' in data:
            for product_data in data["products"]:
                product = Product(
                    Product_ID=product_data["Product_ID"],
                    Product_Name=product_data["Product_Name"],
                    Created_At=parse_datetime(product_data["Created_At"]),
                    Updated_At=parse_datetime(product_data["Updated_At"]),
                    OnMain=product_data.get("OnMain", False),
                    moysklad_connector_products_data=product_data.get("moysklad_connector_products_data"),
                    importance_num=product_data.get("importance_num"),
                    tags=product_data.get("tags")
                )
                session.merge(product)

        session.commit()

        if 'products' in data:
            for product_data in data["products"]:
                for color in product_data.get("colors", []):
                    session.merge(Color(**color))

                for param in product_data.get("parameters", []):
                    session.merge(Parameter(**param))

                for img in product_data.get("images", []):
                    session.merge(Image(**img))

                for rev in product_data.get("reviews", []):
                    session.merge(Review(**rev))

                for video in product_data.get("reviews_video", []):
                    session.merge(ReviewVideo(**video))

                for extra in product_data.get("extras", []):
                    session.merge(Extra(**extra))

                for ex in product_data.get("excluded", []):
                    session.merge(Excluded(**ex))

        session.commit()

    except Exception as e:
        session.rollback()
        logger.error(f"Ошибка при сохранении данных: {e}")
    finally:
        session.close()

def load_and_update_data():
    for url in API_URLS:
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            add_to_bd(data)
        except Exception as e:
            logger.error(f"Ошибка при загрузке с {url}: {e}")
