import mysql.connector
from mysql.connector import errorcode

try:
    # Connect to the MySQL server (change user and password as needed)
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234"  # Replace with your actual MySQL password
    )
    cursor = conn.cursor()

    # Try to create the database
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

except mysql.connector.Error as err:
    print(f"Error: Could not connect to MySQL server.\n{err}")

finally:
    # Ensure connection is closed
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
