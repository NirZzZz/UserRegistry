from create_table import create_connection
from mysql.connector import Error


def create_user(user_name):
    conn = create_connection()
    if conn is not None:
        conn.database = 'users'
        insert_query = "INSERT INTO users (user_name, creation_date) VALUES (%s, NOW());"
        try:
            cursor = conn.cursor()
            cursor.execute(insert_query, (user_name,))
            conn.commit()
            print(f"User '{user_name}' created successfully!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()


def modify_user(user_id, user_name):
    conn = create_connection()
    if conn is not None:
        conn.database = 'users'
        insert_query = "UPDATE users SET user_name = %s WHERE user_id = %s;"
        try:
            cursor = conn.cursor()
            cursor.execute(insert_query, (user_name, user_id))
            conn.commit()
            print(f"Id '{user_id}' modified successfully!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()


def get_user(user_id):
    conn = create_connection()
    if conn is not None:
        conn.database = 'users'
        insert_query = "SELECT * FROM users WHERE user_id = %s;"
        try:
            cursor = conn.cursor()
            cursor.execute(insert_query, (user_id,))
            result = cursor.fetchall()
            for row in result:
                print(row[1])
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
    return result


def delete_user(user_id):
    conn = create_connection()
    if conn is not None:
        conn.database = 'users'
        insert_query = """
        DELETE FROM users WHERE user_id = %s;
        """
        try:
            cursor = conn.cursor()
            cursor.execute(insert_query, (user_id,))
            conn.commit()
            print(f"Id '{user_id}' deleted successfully!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
