import pytest
from your_project.auth import AuthManager

@pytest.fixture(scope="module")
def auth_manager():
    """
    Fixture to create an instance of AuthManager.
    """
    return AuthManager()
