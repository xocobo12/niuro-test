# streamlit_app.py

import streamlit as st
from sqlalchemy.sql import text

# Create the SQL connection to pets_db as specified in your secrets file.
conn = st.connection('test_db', type='sql')

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
        s.execute(
            text('INSERT INTO users (username, password) VALUES (:username, :password)'),
            params={'username': username, 'password': hashed_password}
        )
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
        ("admin", "pbkdf2:sha256:260000$rMQd4BtZ$287442d5d35c95b8819f68d8459e8d8c1c876aac7a1825482bc3c2921f597a42"),
        ("test_user", "pbkdf2:sha256:260000$vGd6bxdR$478cf43df5c7542c12973fa9ecd83d38c86856e8453ea069df49faa4326dd284"),
        ("demo", "pbkdf2:sha256:260000$pKd8cXsY$8943def3d87ff9bb0b9f0486c0c47a2321af2a7caf19377da689ddf3c6872efc")
    ]
    
    for username, hashed_password in test_users:
        try:
            add_user(username, hashed_password)
            print(f"Created fixture user: {username}")
        except ValueError:
            print(f"Fixture user already exists: {username}")

# Initialize the users table and create fixture data when the module is loaded
init_users_table()
create_fixture_data() 