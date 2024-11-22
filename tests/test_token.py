from src.auth import jwt_required


# Test function wrapped with the decorator
@jwt_required
def protected_test_function(username=None, token=None):
    return f"Access granted to {username}"


# Testing the decorator
def test_jwt_required_decorator(auth_manager, credentials):
    # Valid token test
    username, password = credentials
    valid_token = auth_manager.create_token(username)
    try:
        result = protected_test_function(token=valid_token)
        assert result == f"Access granted to {username}"
        print("Valid token test passed.")
    except PermissionError as e:
        print(f"Valid token test failed: {e}")

    # Expired token test
    expired_token = auth_manager.create_token(username, exp_hours=-1)
    try:
        protected_test_function(token=expired_token)
        print("Expired token test failed: Expected an exception.")
    except PermissionError as e:
        assert str(e) == "Token has expired."
        print("Expired token test passed.")

    # Invalid token test
    invalid_token = "invalid.token.string"
    try:
        protected_test_function(token=invalid_token)
        print("Invalid token test failed: Expected an exception.")
    except PermissionError as e:
        assert str(e) == "Invalid token."
        print("Invalid token test passed.")

    # Missing token test
    try:
        protected_test_function()
        print("Missing token test failed: Expected an exception.")
    except PermissionError as e:
        assert str(e) == "A valid token is required for this action."
        print("Missing token test passed.")
