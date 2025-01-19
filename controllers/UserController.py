from flask import jsonify, request
from models.UserModel import User
from config import db
import bcrypt
from flask_jwt_extended import create_access_token, jwt_required
from datetime import timedelta


def login():
  data = request.get_json()
  username = data.get('username')
  password = data.get('password')
  user = User.query.filter_by(username=username).first()
  if not user or not check_password_hash(user.password, password):
    return jsonify({'message': 'Invalid username or password'}), 401
  access_token = create_access_token(identity=user.username, expires_delta=timedelta(hours=20))
  return jsonify({'access_token': access_token})


# Fungsi untuk menghash password
def hash_password(password):
  
    salt = bcrypt.gensalt()

    # Hash password dengan menggunakan salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password

# Fungsi untuk memverifikasi password
def check_password_hash(hashed_password, user_password):
   
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password.encode('utf-8'))

@jwt_required()
def get_users():
    users = User.query.all()  # Mendapatkan semua pengguna dari database
    user_list = []  # Menyimpan detail pengguna

    for user in users:
        user_list.append({
            'id': user.id,
            'username': user.username,
            'fullname': user.fullname,
            'password': user.password  # Anda mungkin ingin menghindari mengirimkan password secara langsung
        })
        
    response = {
        'status': 'success',
        'data': {
            'users': user_list
        },
        'message': 'Users retrieved successfully!'
    }
    
    return jsonify(response),200

# def get_users():
#     users = User.query.all()
#     users =[]
#     for user in users:
#         #add details
#         users.append({
#             'id': user.id,
#             'username': user.username,
#             'fullname': user.fullname,
#             'password' : user.password
#         })
        
#     response ={
#         'status':'success',
#         'data':{
#             'users':users
#         },
#         'message':'Users retrived successfully!'
#     }
#     return jsonify(response),200
@jwt_required()
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error' : 'user not found'}),404
    

    user_data = {
        'id': user.id,
        'username': user.username,
        'fullname': user.fullname,
        'password' : user.password
    }
    
    response ={
        'status':'success',
        'data':{
            'user':user_data
        },
        'message':'User retrieved successfuly!'
    }
    return jsonify(response),200
@jwt_required()
def add_user():
    new_user_data = request.get_json()
    hashed_pw = hash_password(new_user_data['password'])
    new_user = User(
        username = new_user_data['username'],
        password = hashed_pw,
        fullname = new_user_data['fullname']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message' : 'user added successfully!','user':new_user.to_dict()}),201
@jwt_required()
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error':'user not found'}),404
    update_data = request.get_json()
    user.username = update_data.get('username',user.username)
    user.password = update_data.get('password',user.password)
    user.fullname = update_data.get('fullname',user.fullname)
    
    db.session.commit()
    return jsonify({'message' : 'user update successfully!','user' :user.to_dict()})
@jwt_required()
def patch_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error' : 'user not fount'}),404

    patch_data = request.get_json()
    if 'username' in patch_data:
        user.usename = patch_data['username']
        
    if 'password' in patch_data:
        user.password = patch_data['password']
        
    if 'fullname' in patch_data:
        user.fullname = patch_data['fullname']
 
        
    db.session.commit()
    return jsonify({'message':'user partially updated successfully!','user':user.to_dict()})
@jwt_required()
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error' : 'user not fount'}),404
    
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message':'user deleted successfully!'})
