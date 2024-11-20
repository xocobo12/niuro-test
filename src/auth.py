import bcrypt
import jwt
from datetime import datetime, timedelta
from src.db import add_user, get_user_password
from src.hash_utils import hash_password
import os
from dotenv import load_dotenv
from functools import wraps

# Load env variables from .env
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")


class AuthManager:
    """
    A class to manage user authentication and token-based authorization.

    Methods
    -------
    register_user(username, password)
        Registers a new user with an encrypted password.

    authenticate_user(username, password)
        Authenticates a user by verifying their password.

    create_token(username)
        Generates a JWT token for a given username.

    verify_token(token)
        Verifies a JWT token and extracts user information.
    """

    def __init__(self):
        pass

    def register_user(self, username, password):
        """
        Registers a new user with an encrypted password.

        Parameters
        ----------
        username : str
            The username of the new user.
        password : str
            The plain-text password of the new user.

        Returns
        -------
        bool
            True if the registration was successful, False otherwise.
        """
        hashed_password = hash_password(password)
        try:
            add_user(username, hashed_password)
            return True
        except Exception as e:
            print(f"Error registering user: {e}")
            return False

    def authenticate_user(self, username, password):
        """
        Authenticates a user by verifying their password.

        Parameters
        ----------
        username : str
            The username of the user trying to log in.
        password : str
            The plain-text password of the user trying to log in.

        Returns
        -------
        str or None
            JWT token if authentication is successful, None otherwise.
        """
        hashed_password = get_user_password(username)
        checked_password = bcrypt.checkpw(password.encode(), hashed_password)
        if hashed_password and checked_password:
            # Create token if successful
            return self.create_token(username)
        return False

    def create_token(self, username, exp_hours=12):
        """
        Generates a JWT token for a given username.

        Parameters
        ----------
        username : str
            The username for whom to generate the token.

        exp_hours : int
            Number of hours that token lasts

        Returns
        -------
        str
            JWT token as a string.
        """
        exp = datetime.utcnow() + timedelta(hours=exp_hours)
        payload = {
            "username": username,
            "exp": exp.timestamp(),
        }
        return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

    def verify_token(self, token):
        """
        Verifies a JWT token and extracts user information.

        Parameters
        ----------
        token : str
            JWT token to verify.

        Returns
        -------
        str or None
            Username if token is valid, None otherwise.
        """
        try:
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return decoded_token["username"]
        except jwt.ExpiredSignatureError:
            print("Token expired.")
            return None
        except jwt.InvalidTokenError:
            print("Invalid token.")
            return None


def jwt_required(f):
    """
    Decorator that checks for a valid JWT before allowing access.

    Parameters
    ----------
    f : function
        The function to be decorated.

    Returns
    -------
    function
        The wrapped function with JWT verification.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check if token is in session state or request
        token = kwargs.get('token')

        if not token:
            raise PermissionError("A valid token is required for this action.")

        try:
            # Decode the token
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            # Optional: Check expiration or other claims here
            if decoded_token.get("exp") < datetime.utcnow().timestamp():
                raise PermissionError("Token has expired.")
            # Add user info from token to function arguments
            kwargs["username"] = decoded_token.get("username")
        except jwt.ExpiredSignatureError:
            raise PermissionError("Token has expired.")
        except jwt.InvalidTokenError:
            raise PermissionError("Invalid token.")

        return f(*args, **kwargs)

    return decorated_function
