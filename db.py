import pyodbc

def get_db_connection():
    conn_str = (
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=SHRAY\\SQLEXPRESS;'
        'DATABASE=My_Database;'
        'Trusted_Connection=yes;'
    )
    conn = pyodbc.connect(conn_str)
    return conn
