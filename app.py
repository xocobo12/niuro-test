import streamlit as st
import os
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()

# Read the email and password from environment variables
VALID_EMAIL = os.getenv("VALID_EMAIL")
VALID_PASSWORD = os.getenv("VALID_PASSWORD")


# Function to handle login
def login(email, password):
    if email == VALID_EMAIL and password == VALID_PASSWORD:
        return True
    return False


# Main app
def main():
    st.set_page_config(page_title='Registration')
    st.title("Authentification")
    st.write("Please enter your Email and Password")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        st.success(f"Welcome, {VALID_EMAIL}!")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()
    else:
        st.subheader("Login")

        # Email input field
        email = st.text_input("Email", "")

        # Password input field
        password = st.text_input("Password", "", type="password")

        # Login button
        if st.button("Login"):
            if email and password:
                if login(email, password):
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("Invalid email or password.")
            else:
                st.warning("Please enter both email and password.")


if __name__ == "__main__":
    main()
