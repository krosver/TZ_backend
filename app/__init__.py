from flask import Flask
from app.config import Config
from app.extensions import db
from app.api.routes import api_bp
from app.services.scheduler import start_scheduler

from app.models import *

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(api_bp)

    start_scheduler()

    return app
