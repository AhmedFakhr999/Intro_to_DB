#!/usr/bin/python3
"""
Script to create MySQL database 'alx_book_store'
If the database already exists, it won't fail
"""

import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

load_dotenv()

def create_database():
    connection = None

    try:
        DB_HOST = os.getenv("DB_HOST", "localhost")
        DB_USER = os.getenv("DB_USER")
        DB_PASSWORD = os.getenv("DB_PASSWORD")
        DB_NAME = os.getenv("DB_NAME", "alx_book_store")
        DB_PORT = int(os.getenv("DB_PORT", 3306))

        if not (DB_USER and DB_PASSWORD):
            raise RuntimeError("Database credentials not found. Set DB_USER and DB_PASSWORD in .env or environment variables.")

        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT,
            auth_plugin='mysql_native_password'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Use the database name from environment variable
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")

            print(f"Database '{DB_NAME}' created successfully!")

            cursor.close()

    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    except RuntimeError as re:
        print(re)

    finally:
        if connection and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    create_database()