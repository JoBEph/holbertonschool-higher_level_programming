#!/usr/bin/env python3

from flask import jsonify, Flask, request

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"name": "John", "age": 30, "city": "New York"}
}

app = Flask(__name__)


@app.route('/')
def home():
    return '<p>Welcome to the Flask API!</p>'


@app.route('/data')
def get_data():
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/status')
def status():
    return 'OK'


@app.route('/users/<string:username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = {
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }
    return jsonify({
        "message": "User added successfully", "user": users[username]
        }), 201


if __name__ == '__main__':
    PORT = 5000
    app.run(host='localhost', port=PORT, debug=True)
