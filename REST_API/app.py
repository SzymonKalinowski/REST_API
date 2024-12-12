from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}
next_id = 1

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200

@app.route('/users', methods=['POST'])
def create_user():
    global next_id
    user_id = next_id
    data = request.get_json()
    user = {"id": next_id, "name": data["name"], "lastname": data["lastname"]}
    users[next_id] = user
    next_id += 1
    return '', 201
