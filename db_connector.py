from create_table import create_connection
from mysql.connector import Error


def execute_query(query, params=None, fetch=False):
    """ Utility function to handle repetitive query execution logic """
    conn = create_connection()  # Get the connection
    result = None
    if conn is not None:
        conn.database = 'users'  # Use the 'users' database
        try:
            cursor = conn.cursor()
            cursor.execute(query, params)  # Execute the query with parameters
            if fetch:
                result = cursor.fetchall()  # Fetch results if needed
            else:
                conn.commit()  # Commit the changes for non-fetch queries
            return result
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()  # Close cursor
            conn.close()    # Close the connection
    return result


def create_user(user_name):
    """ Create a new user in the users table """
    query = "INSERT INTO users (user_name, creation_date) VALUES (%s, NOW());"
    execute_query(query, (user_name,))
    print(f"User '{user_name}' created successfully!")


def modify_user(user_id, user_name):
    """ Modify an existing user in the users table """
    query = "UPDATE users SET user_name = %s WHERE user_id = %s;"
    execute_query(query, (user_name, user_id))
    print(f"User with ID '{user_id}' modified successfully!")


def get_user(user_id):
    """ Retrieve a user from the users table """
    query = "SELECT * FROM users WHERE user_id = %s;"
    result = execute_query(query, (user_id,), fetch=True)
    if result:
        print(result[0])  # Print the first user found
    return result


def delete_user(user_id):
    """ Delete a user from the users table """
    query = "DELETE FROM users WHERE user_id = %s;"
    execute_query(query, (user_id,))
    print(f"User with ID '{user_id}' deleted successfully!")
