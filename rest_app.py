from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)
mysql = MySQL(app)

# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'your_database'
app.config['MYSQL_HOST'] = 'your_db_host'


@app.route('/users/<int:user_id>', methods=['POST'])
def create_user(user_id):
    cursor = mysql.connection.cursor()

    # Check if the user_id already exists in the database
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    if cursor.fetchone():
        return jsonify({"error": "User ID already exists"}), 500

    # Get the JSON data from the request
    data = request.json
    user_name = data.get('user_name')

    # Validate that user_name is provided
    if not user_name:
        return jsonify({"error": "Missing user_name"}), 400

    # Get the current datetime
    creation_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Insert the new user into the database
    cursor.execute("INSERT INTO users (user_id, user_name, creation_date) VALUES (%s, %s, %s)", (user_id, user_name, creation_date))
    mysql.connection.commit()

    # Close the connection
    cursor.close()

    # Return a success response
    return jsonify({"user_id": user_id, "user_name": user_name, "creation_date": creation_date}), 200


if __name__ == '__main__':
    app.run(debug=True)
