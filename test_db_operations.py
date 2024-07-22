import unittest
import mysql.connector


class TestDatabaseOperations(unittest.TestCase):
    def setUp(self):
        # This method will be executed before each test
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            database='your_database'
        )
        self.cursor = self.conn.cursor()

    def test_table_exists(self):
        # Test to check if the table exists
        self.cursor.execute("SHOW TABLES LIKE 'users';")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)

    def tearDown(self):
        # This method will be executed after each test
        self.conn.close()


if __name__ == '__main__':
    unittest.main()
