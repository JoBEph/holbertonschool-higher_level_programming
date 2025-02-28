#!/usr/bin/env python3

"""basic security for user/admin roles used in the API"""
import os
import datetime
from functools import wraps
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required
from flask_jwt_extended import create_access_token, get_jwt_identity
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY") or "secret_key"
jwt = JWTManager(app)
auth = HTTPBasicAuth()


users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
        },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
        }
    }


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None


def authenticate(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return user
    return None


def role_required(role):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            current_user_name = get_jwt_identity()
            user = users.get(current_user_name)

            if not user or user["role"] != role:
                return jsonify({"error": "Insufficient privileges"}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    auth = request.get_json()
    if not auth or not auth.get('username') or not auth.get('password'):
        return jsonify({"message": "Could not verify"}), 401

    user = authenticate(auth.get('username'), auth.get('password'))
    if not user:
        return jsonify({"message": "Could not verify"}), 401

    token = create_access_token(identity=user['username'], fresh=True)
    return jsonify({'access_token': token}), 200


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def protected_route():
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=['GET'])
@jwt_required()
def admin_access():
    current_user = get_jwt_identity()
    user = users.get(current_user)
    if user["role"] == "admin":
        return "Admin Access: Granted"
    return jsonify({"error": "Admin access required"}), 403


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
