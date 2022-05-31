# bruh
import sqlite3
from sqlite3 import Error

def create_connection(path):
    '''
        Creates a connection to a database named data.sqlite, if not found a new database is created 
    '''
    global connection
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
        print("\n\nConnection to SQLite DB successful.", "\nDatabase: ", path)

    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_read_query(connection, query):

    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


create_connection("data.sqlite")