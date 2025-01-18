from flask import jsonify, request
from models.RatingModel import Rating
from config import db
from flask_jwt_extended import jwt_required

@jwt_required()
def get_ratings():
    ratings = Rating.query.all()
    return jsonify([rating.to_dict() for rating in ratings])

@jwt_required()
def get_rating(id_rate):
    rating = Rating.query.get(id_rate)
    if not rating:
        return jsonify({'status': 'error', 'message': 'Rating not found'}), 404
    return jsonify(rating.to_dict())

@jwt_required()
def add_rating():
    data = request.get_json()
    rating = Rating(nama_rate=data['nama_rate'])  # Using 'nama_rate' for rating name
    db.session.add(rating)
    db.session.commit()
    return jsonify({'message': 'Rating added successfully!', 'rating': rating.to_dict()}), 201

@jwt_required()
def update_rating(id_rate):
    rating = Rating.query.get(id_rate)
    if not rating:
        return jsonify({'status': 'error', 'message': 'Rating not found'}), 404

    data = request.get_json()
    rating.nama_rate = data.get('nama_rate', rating.nama_rate)  # Using 'nama_rate' for rating name

    db.session.commit()
    return jsonify({'message': 'Rating updated successfully!', 'rating': rating.to_dict()})

@jwt_required()
def delete_rating(id_rate):
    rating = Rating.query.get(id_rate)
    if not rating:
        return jsonify({'status': 'error', 'message': 'Rating not found'}), 404

    db.session.delete(rating)
    db.session.commit()
    return jsonify({'message': 'Rating deleted successfully!'})
