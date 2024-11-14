import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from sqlite3 import Connection


# Function to load data from a file
def load_data(file, file_type='csv'):
    """
    Loads data from a file into a Pandas DataFrame.

    Parameters:
        file (File-like): Uploaded file.
        file_type (str): Type of the file ('csv' or 'excel').

    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    try:
        if file_type == 'csv':
            return pd.read_csv(file)
        elif file_type == 'excel':
            return pd.read_excel(file)
        else:
            raise ValueError("Unsupported file format.")
    except Exception as e:
        raise ValueError(f"Error loading file: {e}")


# Function to clean specific columns
def clean_columns(df, columns):
    """
    Removes specified columns from a DataFrame.

    Parameters:
        df (pd.DataFrame): Original DataFrame.
        columns (list): List of column names to drop.

    Returns:
        pd.DataFrame: Modified DataFrame.
    """
    return df.drop(columns=columns, errors='ignore')


# Function to handle missing values
def handle_missing_values(df, strategy='drop'):
    """
    Handles missing values in a DataFrame.

    Parameters:
        df (pd.DataFrame): Original DataFrame.
        strategy (str): 'drop' to remove rows with NaNs, 'fill' to replace them.

    Returns:
        pd.DataFrame: Modified DataFrame.
    """
    if strategy == 'drop':
        return df.dropna()
    elif strategy == 'fill':
        return df.fillna(0)  # Replace NaNs with 0
    else:
        raise ValueError("Unsupported strategy.")


# Function to generate a line chart
def generate_line_chart(df, x, y):
    """
    Generates a line chart for specified x and y columns.

    Parameters:
        df (pd.DataFrame): DataFrame containing the data.
        x (str): Column for the x-axis.
        y (str): Column for the y-axis.

    Returns:
        matplotlib.figure.Figure: Line chart figure.
    """
    fig, ax = plt.subplots()
    ax.plot(df[x], df[y], marker='o')
    ax.set_title(f'{y} vs {x}')
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    return fig


# Function to compute basic statistics
def compute_basic_statistics(df, column):
    """
    Computes basic statistics for a numerical column.

    Parameters:
        df (pd.DataFrame): DataFrame with data.
        column (str): Name of the numerical column.

    Returns:
        dict: Dictionary of basic statistics.
    """
    return {
        'Mean': df[column].mean(),
        'Median': df[column].median(),
        'Max': df[column].max(),
        'Min': df[column].min(),
        'Standard Deviation': df[column].std()
    }


# Function to configure Streamlit default settings
def configure_streamlit():
    """
    Configures default settings for Streamlit.
    """
    import streamlit as st
    st.set_page_config(
        page_title="My Streamlit App",
        page_icon="📊",
        layout="wide"
    )


# Function to create a SQLite database connection
def create_connection(db_path: str) -> Connection:
    """
    Creates a connection to the SQLite database.

    Parameters:
        db_path (str): Path to the SQLite database file.

    Returns:
        sqlite3.Connection: Database connection object.
    """
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        raise RuntimeError(f"Error connecting to database: {e}")


# Function to initialize the database with a table
def initialize_database(conn: Connection, table_schema: str):
    """
    Initializes the database by creating the required tables.

    Parameters:
        conn (sqlite3.Connection): Database connection object.
        table_schema (str): SQL schema for the table creation.

    Returns:
        None
    """
    try:
        cursor = conn.cursor()
        cursor.execute(table_schema)
        conn.commit()
    except sqlite3.Error as e:
        raise RuntimeError(f"Error initializing database: {e}")


# Function to insert data into a table
def insert_data(conn: Connection, table: str, data: tuple):
    """
    Inserts data into a specified table.

    Parameters:
        conn (sqlite3.Connection): Database connection object.
        table (str): Name of the table.
        data (tuple): Data to be inserted as a tuple.

    Returns:
        None
    """
    try:
        cursor = conn.cursor()
        placeholders = ', '.join(['?'] * len(data))
        query = f"INSERT INTO {table} VALUES ({placeholders})"
        cursor.execute(query, data)
        conn.commit()
    except sqlite3.Error as e:
        raise RuntimeError(f"Error inserting data: {e}")


# Function to fetch data from a table
def fetch_data(conn: Connection, query: str):
    """
    Fetches data from the database based on a given query.

    Parameters:
        conn (sqlite3.Connection): Database connection object.
        query (str): SQL query to fetch data.

    Returns:
        list: List of tuples containing the fetched data.
    """
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.Error as e:
        raise RuntimeError(f"Error fetching data: {e}")
