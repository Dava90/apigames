from flask import Blueprint
from controllers.RatingController import get_ratings, get_rating, add_rating, update_rating, delete_rating

rating_bp = Blueprint('rating_bp', __name__)

rating_bp.route('/api/ratings', methods=['GET'])(get_ratings)
rating_bp.route('/api/ratings/<int:id_rate>', methods=['GET'])(get_rating)
rating_bp.route('/api/ratings', methods=['POST'])(add_rating)
rating_bp.route('/api/ratings/<int:id_rate>', methods=['PUT'])(update_rating)
rating_bp.route('/api/ratings/<int:id_rate>', methods=['DELETE'])(delete_rating)
