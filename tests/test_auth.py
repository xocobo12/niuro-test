import pytest
from dotenv import load_dotenv
import os


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
