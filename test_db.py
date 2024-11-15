import streamlit as st
from db import init_db

# Init database
init_db()

# Create the SQL connection to pets_db as specified in your secrets file.
conn = st.connection('test_db', type='sql')

# Query and display the data you inserted
users = conn.query('select * from users')
st.dataframe(users)