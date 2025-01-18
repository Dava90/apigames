from flask import jsonify, request
from models.PlatformModel import Platform
from config import db
from flask_jwt_extended import jwt_required

@jwt_required()
def get_platforms():
    platforms = Platform.query.all()
    return jsonify([platform.to_dict() for platform in platforms])

@jwt_required()
def get_platform(platform_id):
    platform = Platform.query.get(platform_id)
    if not platform:
        return jsonify({'status': 'error', 'message': 'Platform not found'}), 404
    return jsonify(platform.to_dict())

@jwt_required()
def add_platform():
    data = request.get_json()
    platform = Platform(nama_plat=data['nama_plat'])  # mengganti 'name' dengan 'nama_plat'
    db.session.add(platform)
    db.session.commit()
    return jsonify({'message': 'Platform added successfully!', 'platform': platform.to_dict()}), 201

@jwt_required()
def update_platform(platform_id):
    platform = Platform.query.get(platform_id)
    if not platform:
        return jsonify({'status': 'error', 'message': 'Platform not found'}), 404

    data = request.get_json()
    platform.nama_plat = data.get('nama_plat', platform.nama_plat)  # mengganti 'name' dengan 'nama_plat'

    db.session.commit()
    return jsonify({'message': 'Platform updated successfully!', 'platform': platform.to_dict()})

@jwt_required()
def delete_platform(platform_id):
    platform = Platform.query.get(platform_id)
    if not platform:
        return jsonify({'status': 'error', 'message': 'Platform not found'}), 404

    db.session.delete(platform)
    db.session.commit()
    return jsonify({'message': 'Platform deleted successfully!'})