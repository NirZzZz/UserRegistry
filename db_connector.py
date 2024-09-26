from create_table import create_connection
from mysql.connector import Error


# Utility function to handle repetitive query execution logic
def execute_query(query, params=None, fetch=False):
    conn = create_connection()
    result = None
    if conn is not None:
        conn.database = 'users'
        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            if fetch:
                result = cursor.fetchall()
            else:
                conn.commit()
            return result
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
    return result


# Create a new user in the users table
def create_user(user_name):
    query = "INSERT INTO users (user_name, creation_date) VALUES (%s, NOW());"
    execute_query(query, (user_name,))
    print(f"User '{user_name}' created successfully!")


# Modify an existing user in the users table
def modify_user(user_id, user_name):
    query = "UPDATE users SET user_name = %s WHERE user_id = %s;"
    execute_query(query, (user_name, user_id))
    print(f"User with ID '{user_id}' modified successfully!")


# Retrieve a user from the users table
def get_user(user_id):
    query = "SELECT * FROM users WHERE user_id = %s;"
    result = execute_query(query, (user_id,), fetch=True)
    if result:
        print(result[0])
    return result


# Delete a user from the users table
def delete_user(user_id):
    query = "DELETE FROM users WHERE user_id = %s;"
    execute_query(query, (user_id,))
    print(f"User with ID '{user_id}' deleted successfully!")


def get_all_users():
    users_list = []
    query = "SELECT * FROM users;"
    result = execute_query(query, fetch=True)
    rows = result
    for row in rows:
        users_list.append({
            "user_id": row[0],
            "user_name": row[1],
            "creation_date": row[2]
        })
    if result:
        print(result)
    return users_list
