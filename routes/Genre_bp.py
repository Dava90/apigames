from flask import Blueprint
from controllers.GenreController import get_genres, get_genre, add_genre, update_genre, delete_genre

genre_bp = Blueprint('genre_bp', __name__)

genre_bp.route('/api/genres', methods=['GET'])(get_genres)
genre_bp.route('/api/genres/<int:genre_id>', methods=['GET'])(get_genre)
genre_bp.route('/api/genres', methods=['POST'])(add_genre)
genre_bp.route('/api/genres/<int:genre_id>', methods=['PUT'])(update_genre)
genre_bp.route('/api/genres/<int:genre_id>', methods=['DELETE'])(delete_genre)
