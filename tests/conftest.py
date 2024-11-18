import pytest
import os
from src.auth import AuthManager
from dotenv import load_dotenv


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
