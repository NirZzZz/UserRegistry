from flask import Flask, request, jsonify
from db_connector import create_user, modify_user, get_user, delete_user

app = Flask(__name__)


# Handles POST requests to add a new user by extracting 'user_name' from the request.
# Returns a JSON response with the status and added user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_name = data.get('user_name')
    if user_name and user_name.strip():
        try:
            create_user(user_name)
            return jsonify({"status": "ok", "user_added": user_name}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "invalid user_name"}), 500


# Handles GET requests to retrieve a user by user_id.
# Returns the user's name in a JSON response or an error message if the user is not found.
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    try:
        result = get_user(user_id)
        if result:
            user_data = result[0]
            return jsonify({"status": "ok", "user_name": user_data[1]}), 200
        else:
            return jsonify({"status": "error", "reason": "no such id"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Handles PUT requests to update a user's name based on their user_id.
# Returns a success message with the updated user name or an error if no such ID exists.
@app.route('/users/<int:user_id>', methods=['PUT'])
def change_username_by_id(user_id):
    data = request.get_json()
    user_name = data.get('user_name')
    if user_name:
        try:
            modify_user(user_id, user_name)
            return jsonify({"status": "ok", "user_updated": user_name}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"status": "error", "reason": "no such id"}), 500


# Handles DELETE requests to remove a user by user_id.
# Returns a success message with the deleted user_id or an error if no such ID exists.
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_by_id(user_id):
    try:
        delete_user(user_id)
        return jsonify({"status": "ok", "user_deleted": user_id}), 200
    except None:
        return jsonify({"status": "error", "reason": "no such id"}), 500


if __name__ == '__main__':
    app.run(debug=True)
