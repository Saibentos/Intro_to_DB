import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host='localhost',
        user='root',  # Replace with your MySQL username
        password=''   # Replace with your MySQL password
    )
    
    if connection.is_connected():
        cursor = connection.cursor()
        # Create database if not exists
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
        
except Error as e:
    print(f"Error: {e}")
    
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
