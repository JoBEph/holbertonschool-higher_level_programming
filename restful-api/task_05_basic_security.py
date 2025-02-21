#!/usr/bin/env python3

"""basic security for user/admin roles used in the API"""

import datetime
from functools import wraps
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required
from flask_jwt_extended import create_access_token, get_jwt_identity

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

users = [
    {"username":
     "admin", "password": generate_password_hash("password"), "role": "admin"},
    {"username":
     "user", "password": generate_password_hash("password"), "role": "user"}
]


def authenticate(username, password):
    user = next((u for u in users if u["username"] == username and
                check_password_hash(u["password"], password)), None)
    return user


def role_required(role):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            current_user_name = get_jwt_identity()
            current_user = next((
                u for u in users if u["username"] == current_user_name), None
                )
            if not current_user or current_user['role'] != role:
                return jsonify({"error": "Privilèges insuffisants"}), 403
            return f(current_user, *args, **kwargs)
        return wrapper
    return decorator


@app.route('/login', methods=['POST'])
def login():
    auth = request.get_json()
    if not auth or not auth.get('username') or not auth.get('password'):
        return jsonify({"message": "Could not verify"}), 401

    user = authenticate(auth.get('username'), auth.get('password'))
    if not user:
        return jsonify({"message": "Could not verify"}), 401

    token = create_access_token(identity=user['username'], fresh=True)
    return jsonify({'token': token})


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected_route():
    current_user = get_jwt_identity()
    return jsonify({"message": f"Welcome {current_user}!"})


@app.route('/admin', methods=['GET'])
@jwt_required()
@role_required('admin')
def admin_route():
    current_user = get_jwt_identity()
    user = next((u for u in users if u["username"] == current_user), None)
    return jsonify({"message": f"Welcome admin {user['username']}!"})


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
