from create_table import create_connection
from mysql.connector import Error


def create_user(user_name):
    """ Insert a new user into the users table """
    conn = create_connection()  # Call the function to get the connection
    if conn is not None:
        conn.database = 'users'
        insert_query = """
        INSERT INTO users (user_name, creation_date) 
        VALUES (%s, NOW());
        """
        try:
            cursor = conn.cursor()
            cursor.execute(insert_query, (user_name,))
            conn.commit()
            print(f"User '{user_name}' inserted successfully!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()  # Only close cursor if it was created
            conn.close()    # Close the connection


def modify_user(user_id, user_name):
    conn = create_connection()  # Call the function to get the connection
    if conn is not None:
        conn.database = 'users'
        insert_query = """
        UPDATE users
        SET user_name = %s
        WHERE user_id = %s;
        """
        try:
            cursor = conn.cursor()
            cursor.execute(insert_query, (user_name, user_id))
            conn.commit()
            print(f"Id '{user_id}' modified successfully!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()  # Only close cursor if it was created
            conn.close()    # Close the connection


def get_user(user_id):
    conn = create_connection()  # Call the function to get the connection
    if conn is not None:
        conn.database = 'users'
        insert_query = """
        SELECT * FROM users
        WHERE user_id = %s
        """
        try:
            cursor = conn.cursor()
            cursor.execute(insert_query, (user_id,))
            result = cursor.fetchall()  # Fetch all results
            for row in result:
                print(row)
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()  # Only close cursor if it was created
            conn.close()    # Close the connection


if __name__ == '__main__':
    get_user(1)