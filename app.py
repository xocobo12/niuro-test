import streamlit as st
from dotenv import load_dotenv
from src.auth import AuthManager
import jwt


# Load environment variables from the .env file
load_dotenv()

authmanager = AuthManager()


def main():
    st.title("Authentication")
    st.write("Please log in or create an account.")

    # Session state initialization
    if "token" not in st.session_state:
        st.session_state.token = None
        st.session_state.username = None

    if st.session_state.token:
        st.success(f"Welcome, {st.session_state.username}!")
        if st.button("Logout"):
            st.session_state.token = None
            st.session_state.username = None
            st.rerun()
    else:
        # Login or Registration
        tabs = st.tabs(["Login", "Register"])

        # Login Tab
        with tabs[0]:
            st.subheader("Login")
            username = st.text_input("Username", key="login_username")
            password = st.text_input("Password",
                                     type="password", key="login_password"
                                     )

            if st.button("Login"):
                if username and password:
                    jwtoken = authmanager.authenticate_user(username, password)
                    if jwtoken:
                        payload = jwt.decode(jwtoken, options={"verify_signature": False})
                        st.session_state.token = jwtoken
                        st.session_state.username = payload["username"]
                    else:
                        st.error("Invalid username or password.")
                else:
                    st.warning("Please enter both username and password.")

        # Registration Tab
        with tabs[1]:
            st.subheader("Register")
            new_username = st.text_input("New Username",
                                         key="register_username")
            new_password = st.text_input("New Password", type="password",
                                         key="register_password")

            if st.button("Register"):
                if new_username and new_password:
                    if authmanager.register_user(new_username, new_password):
                        st.success("User created successfully! Please log in.")
                    else:
                        st.error(
                            "Failed to create user. Name might already exist."
                            )
                else:
                    st.warning("Please fill in all fields.")


if __name__ == "__main__":
    main()
