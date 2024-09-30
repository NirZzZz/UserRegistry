import mysql.connector
from mysql.connector import Error
import os
import time


# Create a database connection
def create_connection():
    conn = None
    max_retries = 10
    for attempt in range(max_retries):
        try:
            print(f"Attempt {attempt + 1} to connect to the database...")
            conn = mysql.connector.connect(
                host=os.getenv('DATABASE_HOST', 'db'),
                port=int(os.getenv('DATABASE_PORT', 3306)),
                user=os.getenv('DATABASE_USER', 'root'),
                password=os.getenv('DATABASE_PASSWORD', 'adminadmin')
            )
            if conn.is_connected():
                print("Successfully connected to the MySQL database.")
                return conn
        except Error as e:
            print(f"Error: {e}. Retrying in 5 seconds...")
            time.sleep(5)
    print("Failed to connect to the MySQL database after several attempts.")
    return conn


# Create a database if it doesn't exist
def create_database(conn):
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


# Create a table in the database
def create_table(conn):
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


# Close the database connection
def close_connection(conn):
    if conn and conn.is_connected():
        conn.close()
        print("Connection closed.")


# Main execution
if __name__ == '__main__':
    connection = create_connection()
    if connection is not None:
        create_database(connection)
        connection.database = 'users'
        create_table(connection)
        close_connection(connection)
