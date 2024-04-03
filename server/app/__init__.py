# __init__.py
from flask import Flask
from .routes.card import card_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(card_bp, url_prefix='/cards')
    return app
