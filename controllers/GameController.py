from flask import jsonify, request
from models.GameModel import Game
from models.GenreModel import Genre
from models.DeveloperModel import Developer
from config import db
from flask_jwt_extended import jwt_required
from sqlalchemy import func

# @jwt_required()
# def get_games():
#     games = Game.query.all()
#     return jsonify([game.to_dict() for game in games])

@jwt_required()
def get_games():
    games = Game.query.order_by(func.random()).limit(10).all()
    return jsonify([game.to_dict() for game in games])
@jwt_required()
def get_game(game_id):
    game = Game.query.get(game_id)
    if not game:
        return jsonify({'status': 'error', 'message': 'Game not found'}), 404
    return jsonify(game.to_dict())

@jwt_required()
def add_game():
    data = request.get_json()
    game = Game(
        name=data['name'],
        released=data['released'],
        genre=data['genre'],
        developer=data['developer'],
        publisher=data['publisher'],
        score=data['score'],
        rating=data['rating'],
        platform=data['platforms']
    )
    db.session.add(game)
    db.session.commit()
    return jsonify({'message': 'Game added successfully!', 'game': game.to_dict()}), 201

@jwt_required()
def update_game(game_id):
    game = Game.query.get(game_id)
    if not game:
        return jsonify({'status': 'error', 'message': 'Game not found'}), 404

    data = request.get_json()
    game.name = data.get('name', game.name)
    game.released = data.get('released', game.released)
    game.genre = data.get('genre', game.genre)
    game.developer = data.get('developer', game.developer)
    game.publisher = data.get('publisher', game.publisher)
    game.score = data.get('score', game.score)
    game.rating = data.get('rating', game.rating)
    game.platform = data.get('platform', game.platform)

    db.session.commit()
    return jsonify({'message': 'Game updated successfully!', 'game': game.to_dict()})

@jwt_required()
def patch_game(game_id):
    game = Game.query.get(game_id)
    if not game:
        return jsonify({'status': 'error', 'message': 'Game not found'}), 404

    data = request.get_json()

    if 'name' in data:
        game.name = data['name']
    if 'released' in data:
        game.released = data['released']
    if 'genre' in data:
        game.genre = data['genre']
    if 'developer' in data:
        game.developer = data['developer']
    if 'publisher' in data:
        game.publisher = data['publisher']
    if 'score' in data:
        game.score = data['score']
    if 'rating' in data:
        game.rating = data['rating']
    if 'platform' in data:
        game.platform = data['platform']

    db.session.commit()
    return jsonify({'message': 'Game updated successfully!', 'game': game.to_dict()})

@jwt_required()
def delete_game(game_id):
    game = Game.query.get(game_id)
    if not game:
        return jsonify({'status': 'error', 'message': 'Game not found'}), 404

    db.session.delete(game)
    db.session.commit()
    return jsonify({'message': 'Game deleted successfully!'})
