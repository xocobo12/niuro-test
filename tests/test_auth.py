from src.auth import AuthManager

# Crear una instancia de AuthManager
auth_manager = AuthManager()

# Prueba de registro de usuario
print("Testing user registration...")
username = "test_user"
password = "password123"
is_registered = auth_manager.register_user(username, password)

# Intentar registrar el mismo usuario nuevamente
try:
    auth_manager.register_user(username, password)
except Exception as e:
    print(f"Error as expected when registering the same user: {e}")

# Prueba de autenticación de usuario
print("\nTesting user authentication...")
token = auth_manager.authenticate_user(username, password)
print(f"Authentication successful, token received: {token is not None}")  # Debería ser True

# Prueba de autenticación con una contraseña incorrecta
token = auth_manager.authenticate_user(username, "wrong_password")
print(f"Authentication with wrong password: {token is None}")  # Debería ser True

# Prueba de verificación de token
print("\nTesting token verification...")
if token := auth_manager.authenticate_user(username, password):
    verified_username = auth_manager.verify_token(token)
    print(f"Token verified, username extracted: {verified_username == username}")  # Debería ser True
else:
    print("Failed to authenticate user for token verification.")
