import streamlit as st
import pandas as pd

def main():
    st.title("Process Tracking Tool")

    # Initialize session state to store previous entries
    if 'previous_entries' not in st.session_state:
        st.session_state.previous_entries = []

    # Text input boxes with placeholders
    h_number = st.text_input("Scan your H number", value="", placeholder="Scan your H number")
    order_number = st.text_input("Scan the Planned Order Number", value="", placeholder="Scan the Planned Order Number")
    line_id = st.text_input("Scan the Line ID", value="", placeholder="Scan the Line ID")
    job_quantity = st.number_input("Scan the Job Quantity", min_value=1, step=1, value=1)
    serial_number = st.text_input("Scan the Product Serial Number", value="", placeholder="Scan the Product Serial Number")

    # Store entries if all fields are filled
    if h_number and order_number and line_id and job_quantity and serial_number:
        store_entry(serial_number)
        st.success("Entry submitted successfully!")

    # Display table of previous entries for serial numbers
    display_previous_entries()

def store_entry(serial_number):
    st.session_state.previous_entries.append(serial_number)

def display_previous_entries():
    if len(st.session_state.previous_entries) > 0:
        st.subheader("Previous Entries for Serial Numbers")
        df = pd.DataFrame({"Serial Number": st.session_state.previous_entries})
        st.table(df)

if __name__ == "__main__":
    main()