import pytest
from src.auth import AuthManager
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
        raise ValueError("Username or password is not set in the env vars.")
    return username, password


def test_authenticate_user(auth_manager, credentials):
    """
    Test user authentication with correct credentials.
    """
    username, password = credentials
    # Authenticate user
    token = auth_manager.authenticate_user(username, password)
    auth_success = token is not False
    assert auth_success, "Authentication failed with correct credentials"


def test_authenticate_user_wrong_password(auth_manager, credentials):
    """
    Test user authentication with an incorrect password.
    """
    username, _ = credentials

    # Attempt to authenticate with an incorrect password
    token = auth_manager.authenticate_user(username, "wrong_password")
    auth_fail = token is False
    assert auth_fail, "Authentication should fail with an incorrect password."
