from flask import Flask, request, jsonify
from db_connector import create_user, modify_user, get_user, delete_user

app = Flask(__name__)


@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()  # Get the JSON payload from the POST request
    user_name = data.get('user_name')
    if user_name:
        try:
            create_user(user_name)  # Call the create_user function
            return jsonify({'{“status”: “ok”, “user_added”: <USER_NAME>}'}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify('{“status”: “error”, “reason”: ”id already exists”}'), 500


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    try:
        result = get_user(user_id)  # Call the get_user function
        if result:
            user_data = result[0]  # Get the first tuple from the list
            return jsonify({
                "user_id": user_data[0],
                "user_name": user_data[1],
                "creation_date": user_data[2]
            }), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
