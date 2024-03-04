import streamlit as st
import pyodbc
import psycopg2
import pandas as pd
import numpy as np


hostname = 'localhost'
database = 'Honeywell Data Project'
username = 'postgres'
pwd = 'password'
port_id = 5432
conn = None
cur = None

try:
    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id)

    cur = conn.cursor()

except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

#st.set_page_config(layout="wide")       #Makes Page stretch Left to Right

st.title("Process Tracking Tool")
st.write("This app is used to provide <b>Traceability</b> for the manufacturing process.",
         unsafe_allow_html=True)
h_number = st.text_input(label="", placeholder="Scan your H-Number")
PO_number = st.text_input(label="", placeholder="Scan the Planned Order Number")
Line_ID = st.text_input(label="", placeholder="Scan the Line ID")
SN = st.text_input(label="", placeholder="Scan the Products Serial Number")
df = pd.DataFrame()
