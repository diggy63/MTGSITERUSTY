from flask import Blueprint
from app.controllers.card_controller import get_cards_exact, get_cards_contain


card_bp = Blueprint('card', __name__)

@card_bp.route('/exact/<keyword>', methods=['GET'])
def get_cards_route_exact(keyword):
    return get_cards_exact(keyword)

@card_bp.route('/contain/<keyword>', methods=['GET'])
def get_cards_route_contain(keyword):
    return get_cards_contain(keyword)