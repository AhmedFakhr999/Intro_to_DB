#!/usr/bin/python3
"""
Script to create MySQL database 'alx_book_store'
If the database already exists, it won't fail
"""

import os
import mysql.connector

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("Warning: python-dotenv not installed. Using default values.")
    print("Install with: pip install python-dotenv")

def create_database():
    connection = None

    try:
        DB_HOST = os.getenv("DB_HOST", "localhost")
        DB_USER = os.getenv("DB_USER", "root")
        DB_PASSWORD = os.getenv("DB_PASSWORD", "Program512_121")
        DB_NAME = os.getenv("DB_NAME", "alx_book_store")
        DB_PORT = int(os.getenv("DB_PORT", 3306))

        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT,
            auth_plugin='mysql_native_password'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

            cursor.close()

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        
    finally:
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()