import pytest
from src.auth import AuthManager
from dotenv import load_dotenv
import os
import streamlit as st


@pytest.fixture(scope="module")
def setup_env_and_auth_manager():
    # Load environment variables from .env file
    load_dotenv()

    # Validate environment variables
    username = os.getenv("NEW_USER")
    password = os.getenv("NEW_PASSWORD")
    if not username or not password:
        pytest.fail("Username or password is not set in the environment variables.")

    # Create SQL connection (mocking Streamlit connection in a real test environment)
    #conn = st.connection('test_db', type='sql')

    # Return initialized auth manager and credentials
    return username, password


def test_user_registration(setup_env_and_auth_manager, auth_manager):
    username, password = setup_env_and_auth_manager

    # Test user registration
    is_registered = auth_manager.register_user(username, password)
    assert is_registered, "User registration failed"

    # Attempt to register the same user again, expecting an exception
    reregister = auth_manager.register_user(username, password)
    assert not reregister, "User created twice"

