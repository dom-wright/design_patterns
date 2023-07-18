'''
Singleton

A Singleton class restricts the instantiation of a class to one object, which should be globally accessible in the program. New instances can be created as usual but the __new__ function will return the same instance every time.

It is useful where only one instance is needed and should be used by all users e.g. an open connection to a database, or a single file instance that two threads should work on.
'''


import sqlite3


class DatabaseConnectionSingleton:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def connect(self, database_name):
        # Connect to the database
        connection = sqlite3.connect(database_name)
        return connection

    def execute_query(self, query):
        # Execute a database query
        pass

    def close_connection(self, connection):
        # Close the database connection
        connection.close()


# Usage example
db_conn1 = DatabaseConnectionSingleton()
db_conn2 = DatabaseConnectionSingleton()

print(db_conn1 is db_conn2)  # Output: True

connection1 = db_conn1.connect("example.db")
connection2 = db_conn2.connect("example.db")

print(connection1 is connection2)  # Output: True

# Perform database operations using the connections
db_conn1.execute_query("SELECT * FROM table1")
db_conn2.execute_query("INSERT INTO table1 VALUES (1, 'example')")

db_conn1.close_connection(connection1)
db_conn2.close_connection(connection2)
