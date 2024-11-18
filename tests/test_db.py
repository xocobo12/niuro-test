from streamlit.testing.v1 import AppTest
from src.db import init_db


def app_script():
    import streamlit as st

    # Create the SQL connection to pets_db as specified in your secrets file.
    conn = st.connection('test_db', type='sql')
    # Query and display the data you inserted
    users = conn.query('select * from users')
    st.dataframe(users)


# Create the SQL connection to pets_db as specified in your secrets file.
# Init database
init_db()
at = AppTest.from_function(app_script)
at.run()
assert at.dataframe[0].value.columns is not None
