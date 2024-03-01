import streamlit as st
#import functions

#st.set_page_config(layout="wide")       #Makes Page stretch Left to Right

st.title("Process Tracking Tool")
st.write("This app is used to provide <b>Traceability</b> for process.",
         unsafe_allow_html=True)
st.text_input(label="", placeholder="Scan your H-Number")
st.text_input(label="", placeholder="Scan the Planned Order Number")
st.text_input(label="", placeholder="Scan the Line ID")

