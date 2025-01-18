from flask import Blueprint
from controllers.GameController import get_games, get_game, add_game, update_game, patch_game, delete_game

game_bp = Blueprint('game_bp', __name__)

game_bp.route('/api/games', methods=['GET'])(get_games)
game_bp.route('/api/games/<int:game_id>', methods=['GET'])(get_game)
game_bp.route('/api/games', methods=['POST'])(add_game)
game_bp.route('/api/games/<int:game_id>', methods=['PUT'])(update_game)
game_bp.route('/api/games/<int:game_id>', methods=['PATCH'])(patch_game)
game_bp.route('/api/games/<int:game_id>', methods=['DELETE'])(delete_game)


# from flask import Blueprint
# from flask_restx import Api, Resource, fields
# from controllers.GameController import get_games, get_game, add_game, update_game, patch_game, delete_game
# from flask_jwt_extended import jwt_required

# # Membuat Blueprint untuk game
# game_bp = Blueprint('game_bp', __name__)

# # Membuat instance Api untuk blueprint ini
# api = Api(game_bp)

# # Mendefinisikan model untuk game (untuk dokumentasi Swagger)
# game_model = api.model('Game', {
#     'game_id': fields.Integer(required=True, description='ID of the game'),
#     'name': fields.String(required=True, description='Name of the game'),
#     'release': fields.String(required=True, description='Release date of the game'),
#     'genre': fields.String(description='Genre of the game'),
#     'developer': fields.String(description='Developer of the game'),
#     'publisher': fields.String(description='Publisher of the game'),
#     'platforms': fields.List(fields.String, description='Platforms available for the game')
# })

# # Mendefinisikan rute untuk mengambil semua game
# @api.route('/api/games')
# class GameList(Resource):
#     @api.marshal_list_with(game_model)  # Menyertakan model Game untuk dokumentasi
#     # @jwt_required()  # Endpoint ini memerlukan otentikasi JWT
#     def get(self):
#         """
#         Mengambil daftar semua game
#         """
#         return get_games()

#     @api.expect(game_model)  # Memastikan data yang diterima sesuai dengan model
#     # @jwt_required()  # Endpoint ini memerlukan otentikasi JWT
#     def post(self):
#         """
#         Menambahkan game baru
#         """
#         return add_game()

# # Mendefinisikan rute untuk mengambil, memperbarui, atau menghapus game berdasarkan ID
# @api.route('/api/games/<int:game_id>')
# class GameDetail(Resource):
#     @api.marshal_with(game_model)  # Menyertakan model Game untuk dokumentasi
#     # @jwt_required()  # Endpoint ini memerlukan otentikasi JWT
#     def get(self, game_id):
#         """
#         Mengambil detail game berdasarkan ID
#         """
#         return get_game(game_id)

#     @api.expect(game_model)  # Memastikan data yang diterima sesuai dengan model
#     # @jwt_required()  # Endpoint ini memerlukan otentikasi JWT
#     def put(self, game_id):
#         """
#         Memperbarui data game berdasarkan ID
#         """
#         return update_game(game_id)

#     @api.expect(game_model)  # Memastikan data yang diterima sesuai dengan model
#     # @jwt_required()  # Endpoint ini memerlukan otentikasi JWT
#     def patch(self, game_id):
#         """
#         Memperbarui sebagian data game berdasarkan ID
#         """
#         return patch_game(game_id)

#     # @jwt_required()  # Endpoint ini memerlukan otentikasi JWT
#     def delete(self, game_id):
#         """
#         Menghapus game berdasarkan ID
#         """
#         return delete_game(game_id)
