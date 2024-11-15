import streamlit as st


# Hardcoded email and password for demonstration
VALID_EMAIL = "user@example.com"
VALID_PASSWORD = "password123"


# Function to handle login
def login(email, password):
    if email == VALID_EMAIL and password == VALID_PASSWORD:
        return True
    return False


# Main app
def main():
    st.set_page_config(page_title='Formulario de Registro')
    st.title("Autentificación")
    st.write("Porfavor ingrese su Email y contraseña")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        st.success(f"Welcome, {VALID_EMAIL}!")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.experimental_rerun()
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
                    st.experimental_rerun()
                else:
                    st.error("Invalid email or password.")
            else:
                st.warning("Please enter both email and password.")


if __name__ == "__main__":
    main()
