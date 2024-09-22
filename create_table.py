import mysql.connector
from mysql.connector import Error


def create_connection():
    """ Create a database connection """
    conn = None
    try:
        # Connect without specifying a database
        conn = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='adminadmin'
        )
        print("Connection successful!")
    except Error as e:
        print(f"Error: {e}")
    return conn


def create_database(conn):
    """ Create a database if it doesn't exist """
    create_db_query = "CREATE DATABASE IF NOT EXISTS users;"
    try:
        cursor = conn.cursor()
        cursor.execute(create_db_query)
        conn.commit()
        print("Database created successfully (if it didn't exist).")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


def create_table(conn):
    """ Create a table in the database """
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        user_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL UNIQUE,
        user_name VARCHAR(50) NOT NULL,
        creation_date VARCHAR(50) NOT NULL
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        conn.commit()
        print("Table created successfully!")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


def close_connection(conn):
    """ Close the database connection """
    if conn and conn.is_connected():
        conn.close()
        print("Connection closed.")


# Main execution
if __name__ == '__main__':
    connection = create_connection()
    if connection is not None:
        create_database(connection)  # Create the database
        # Reconnect to the specific database
        connection.database = 'users'  # Switch to the new database
        create_table(connection)  # Create the table
        close_connection(connection)
