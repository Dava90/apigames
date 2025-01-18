from flask import jsonify, request
from models.GenreModel import Genre
from config import db
from flask_jwt_extended import jwt_required

@jwt_required()
def get_genres():
    genres = Genre.query.all()
    return jsonify([genre.to_dict() for genre in genres])

@jwt_required()
def get_genre(genre_id):
    genre = Genre.query.get(genre_id)
    if not genre:
        return jsonify({'status': 'error', 'message': 'Genre not found'}), 404
    return jsonify(genre.to_dict())

@jwt_required()
def add_genre():
    data = request.get_json()
    # Validasi input
    if not data.get('name'):
        return jsonify({'status': 'error', 'message': 'Name is required'}), 400
    
    genre = Genre(name=data['name'])
    db.session.add(genre)
    db.session.commit()
    return jsonify({'message': 'Genre added successfully!', 'genre': genre.to_dict()}), 201

@jwt_required()
def update_genre(genre_id):
    genre = Genre.query.get(genre_id)
    if not genre:
        return jsonify({'status': 'error', 'message': 'Genre not found'}), 404

    data = request.get_json()
    genre.name = data.get('name', genre.name)  # Hanya memperbarui nama jika ada

    db.session.commit()
    return jsonify({'message': 'Genre updated successfully!', 'genre': genre.to_dict()})

@jwt_required()
def delete_genre(genre_id):
    genre = Genre.query.get(genre_id)
    if not genre:
        return jsonify({'status': 'error', 'message': 'Genre not found'}), 404

    db.session.delete(genre)
    db.session.commit()
    return jsonify({'message': 'Genre deleted successfully!'})