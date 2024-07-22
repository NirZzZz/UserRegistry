import mysql.connector


def create_table():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        database="your_database"
    )
    cursor = db_connection.cursor()
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        user_id INT PRIMARY KEY,
        user_name VARCHAR(50) NOT NULL,
        creation_date VARCHAR(50) NOT NULL
    );
    """
    cursor.execute(create_table_sql)
    db_connection.commit()
    print("Table created successfully.")
    cursor.close()
    db_connection.close()


if __name__ == '__main__':
    create_table()
