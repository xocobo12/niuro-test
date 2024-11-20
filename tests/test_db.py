import streamlit as st
from src.db import DBClient


def test_users_table(db_client):
    #import streamlit as st
    # Query and display the data you inserted
    users = db_client.conn.query('select * from users')
    st_df = st.dataframe(users)
    assert st_df is not None, "Users table doesn't exist"
