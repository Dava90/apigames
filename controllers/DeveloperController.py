from flask import jsonify, request
from models.DeveloperModel import Developer
from config import db
from flask_jwt_extended import jwt_required

@jwt_required()
def get_developers():
    developers = Developer.query.all()
    return jsonify([developer.to_dict() for developer in developers])

@jwt_required()
def get_developer(id_dev):
    developer = Developer.query.get(id_dev)
    if not developer:
        return jsonify({'status': 'error', 'message': 'Developer not found'}), 404
    return jsonify(developer.to_dict())

@jwt_required()
def add_developer():
    data = request.get_json()
    developer = Developer(nama_dev=data['nama_dev'])  # Using 'name' as per the column in the model
    db.session.add(developer)
    db.session.commit()
    return jsonify({'message': 'Developer added successfully!', 'developer': developer.to_dict()}), 201

@jwt_required()
def update_developer(id_dev):
    developer = Developer.query.get(id_dev)
    if not developer:
        return jsonify({'status': 'error', 'message': 'Developer not found'}), 404

    data = request.get_json()
    developer.nama_dev = data.get('nama_dev', developer.nama_dev)  # Ensure the 'name' field is updated
    
    db.session.commit()
    return jsonify({'message': 'Developer updated successfully!', 'developer': developer.to_dict()})

@jwt_required()
def patch_developer(id_dev):
    developer = Developer.query.get(id_dev)
    if not developer:
        return jsonify({'error': 'Developer not found'}), 404

    updated_data = request.get_json()

    # Update only the fields that exist in the request
    if 'nama_dev' in updated_data:
        developer.nama_dev = updated_data['nama_dev']  # Update 'name' field
    
    db.session.commit()
    return jsonify({'message': 'Developer updated successfully!', 'developer': developer.to_dict()})

@jwt_required()
def delete_developer(id_dev):
    developer = Developer.query.get(id_dev)
    if not developer:
        return jsonify({'status': 'error', 'message': 'Developer not found'}), 404

    db.session.delete(developer)
    db.session.commit()
    return jsonify({'message': 'Developer deleted successfully!'})
