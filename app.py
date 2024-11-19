import streamlit as st
from dotenv import load_dotenv
from src.auth import AuthManager


# Load environment variables from the .env file
load_dotenv()

authmanager = AuthManager()
# Main app


def main():
    st.set_page_config(page_title='Registration')
    st.title("Authentification")
    st.write("Please enter User name and Password")

    username = None

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        st.success(f"Welcome, {username}!")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()
    else:
        st.subheader("Login")

        # username input field
        username = st.text_input("username", "")

        # Password input field
        password = st.text_input("Password", "", type="password")

        # Login button
        if st.button("Login"):
            if username and password:
                if authmanager.authenticate_user(username, password):
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("Invalid email or password.")
            else:
                st.warning("Please enter both email and password.")


if __name__ == "__main__":
    main()
