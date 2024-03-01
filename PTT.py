import streamlit as st
import pyodbc

# conn = st.connection('pets_db', type='sql')
# with conn.session as s:



#import functions

#st.set_page_config(layout="wide")       #Makes Page stretch Left to Right

st.title("Process Tracking Tool")
st.write("This app is used to provide <b>Traceability</b> for process.",
         unsafe_allow_html=True)
st.text_input(label="", placeholder="Scan your H-Number")
st.text_input(label="", placeholder="Scan the Planned Order Number")
st.text_input(label="", placeholder="Scan the Line ID")

import streamlit as st

conn = st.experimental_connection('pets_db', type='sql')
pet_owners = conn.query('select * from pet_owners')
st.dataframe(pet_owners)