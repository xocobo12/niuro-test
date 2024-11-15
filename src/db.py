import streamlit as st
from sqlalchemy.sql import text
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
db_name = os.getenv('DB_NAME')

# Create the SQLite connection using DB_NAME from .env
conn = st.connection(db_name, type='sql')


def init_users_table():
    """Initialize the users table if it doesn't exist"""
    with conn.session as s:
        s.execute(text('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            );
        '''))
        s.commit()


def add_user(username, hashed_password):
    """
    Add a new user to the database.
    Raises ValueError if user already exists.
    """
    with conn.session as s:
        # Check if user exists
        result = s.execute(
            text('SELECT username FROM users WHERE username = :username'),
            params={'username': username}
        ).fetchone()

        if result:
            raise ValueError("User already exists.")

        # Add new user
        query = text(
            (
                "INSERT INTO users (username, password) "
                "VALUES (:username, :password)"
            )
        )
        params = {
                  'username': username,
                  'password': hashed_password,
                 }

        s.execute(query, params=params)
        s.commit()


def get_user_password(username):
    """
    Retrieve a user's hashed password from the database.
    Returns None if user doesn't exist.
    """
    with conn.session as s:
        result = s.execute(
            text('SELECT password FROM users WHERE username = :username'),
            params={'username': username}
        ).fetchone()

        return result[0] if result else None


def create_fixture_data():
    """
    Create three test users in the database.
    Only creates them if they don't already exist.
    """
    test_users = [
        (os.getenv("TEST_USER"), os.getenv("TEST_PASSWORD")),
    ]

    for username, hashed_password in test_users:
        try:
            add_user(username, hashed_password)
            print(f"Created fixture user: {username}")
        except ValueError:
            print(f"Fixture user already exists: {username}")


def init_db():
    """
    Initialize the db by creating the users table and adding fixture data.
    """
    init_users_table()
    create_fixture_data()
