from flask import Blueprint, jsonify, abort, request
from ..models import User, db, Tweet, likes_table
import hashlib
import secrets

def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    users = User.query.all() # ORM performs SELECT query
    result = []
    for u in users:
        result.append(u.serialize()) # serialize each user
    return jsonify(result) # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    u = User.query.get_or_404(id)
    return jsonify(u.serialize())

@bp.route('', methods=['POST'])
def create():
    # req body must contain uusername and password
    if 'username' not in request.json or 'password' not in request.json:
        return abort(400)
    #username must have at least 3 characters
    if len(request.json['username']) < 3 or len(request.json['password']) < 8:
        return abort(400)
    # construct User
    u = User(
        username=request.json['username'],
        password=request.json['password']
    )
    
    password = scramble(request.json['password'])
    
    db.session.add(u) # prepare CREATE statement
    db.session.commit() # execute CREATE statement
    return jsonify(u.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = User.query.get_or_404(id)
    try:
        db.session.delete(u)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except Exception as e:
        # something went wrong :(
        return jsonify(False), 500
    
    
    
@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    u = User.query.get_or_404(id)
    
    if 'username' not in request.json and 'password' not in request.json:
        return abort(400, description="No data provided to update")
    
    if 'username' in request.json:
        username = request.json['username']
        if len(username) < 3:
            return abort(400, description="Username must be at least 3 characters")
        u.username = username
        
    if 'password' in request.json:
        password = request.json['password']
        if len(password) < 8:
            return abort(400, description="Password must be at least 8 characters")
        u.password = scramble(password)  # Scramble the password
    
    try:
        db.session.commit()
        return jsonify(u.serialize())  # Return the updated user record
    except Exception as e:
        db.session.rollback()  # Rollback the transaction in case of error
        return jsonify({'error': str(e)}), 500
    
    
@bp.route('/<int:id>/liked_tweets', methods=['GET'])
def liked_tweets(id: int):
    u = User.query.get_or_404(id)  # Look up the user by ID
    result = []
    for t in u.liked_tweets:  # Access the liked tweets
        result.append(t.serialize())  # Serialize each tweet
    return jsonify(result)
