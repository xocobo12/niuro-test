import pytest
from src.auth import AuthManager
from src.hash_utils import hash_password
from dotenv import load_dotenv
import os

@pytest.fixture(scope="module")
def auth_manager():
    """
    Fixture to create an instance of AuthManager.
    """
    return AuthManager()

@pytest.fixture(scope="module")
def credentials():
    """
    Fixture to load credentials from environment variables.
    """
    load_dotenv()
    username = os.getenv("USER_1")
    password = os.getenv("PASSWORD_1")
    if not username or not password:
        raise ValueError("Username or password is not set in the environment variables.")
    return username, password

def test_authenticate_user(auth_manager, credentials):
    """
    Test user authentication with correct credentials.
    """
    username, password = credentials
    # Authenticate user
    token = auth_manager.authenticate_user(username, password)
    assert token is not False, "Authentication failed with correct credentials."

def test_authenticate_user_wrong_password(auth_manager, credentials):
    """
    Test user authentication with an incorrect password.
    """
    username, _ = credentials

    # Attempt to authenticate with an incorrect password
    token = auth_manager.authenticate_user(username, "wrong_password")
    assert token is False, "Authentication should fail with an incorrect password."
