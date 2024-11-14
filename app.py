import streamlit as st
# from utils import *
# from db import *
# from auth import *


st.set_page_config(page_title='Formulario de Niuro ', layout='wide')

st.title("Hello, Niuro!")
st.write("Welcome to your first Streamlit app.")
if st.button("Presione para agregar un nuevo registro"):
    pass

with st.form('report'):
    st.write("### Report Details")
    col1, col2 = st.columns(2)

    report_title = col1.text_input("Enter report title")
    report_author = col1.text_input("Enter the report author's name")
    report_date = col2.date_input("Select a date for the report")
    report_client = col2.text_input("Enter the client's name")

    sect_col1, sect_col2 = st.columns(2)

    sect_col1.write("### Section Details")
    section_title = sect_col1.text_input("Enter section title")
    section_text_summary = sect_col1.text_area("Section Summary")

    if st.form_submit_button('Generate'):
        generate_report(report_title)
