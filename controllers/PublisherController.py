from flask import jsonify, request
from models.PublisherModel import Publisher
from config import db
from flask_jwt_extended import jwt_required

@jwt_required()
def get_publishers():
    publishers = Publisher.query.all()
    return jsonify([publisher.to_dict() for publisher in publishers])

@jwt_required()
def get_publisher(publisher_id):
    publisher = Publisher.query.get(publisher_id)
    if not publisher:
        return jsonify({'status': 'error', 'message': 'Publisher not found'}), 404
    return jsonify(publisher.to_dict())

@jwt_required()
def add_publisher():
    data = request.get_json()
    publisher = Publisher(nama_pub=data['nama_pub'])  # Using 'nama_pub' instead of 'name'
    db.session.add(publisher)
    db.session.commit()
    return jsonify({'message': 'Publisher added successfully!', 'publisher': publisher.to_dict()}), 201

@jwt_required()
def update_publisher(publisher_id):
    publisher = Publisher.query.get(publisher_id)
    if not publisher:
        return jsonify({'status': 'error', 'message': 'Publisher not found'}), 404

    data = request.get_json()
    publisher.nama_pub = data.get('nama_pub', publisher.nama_pub)  # Using 'nama_pub' instead of 'name'

    db.session.commit()
    return jsonify({'message': 'Publisher updated successfully!', 'publisher': publisher.to_dict()})

@jwt_required()
def delete_publisher(publisher_id):
    publisher = Publisher.query.get(publisher_id)
    if not publisher:
        return jsonify({'status': 'error', 'message': 'Publisher not found'}), 404

    db.session.delete(publisher)
    db.session.commit()
    return jsonify({'message': 'Publisher deleted successfully!'})