import streamlit as st
import pandas as pd

def main():
    st.title("Process Tracking Tool")

    # Initialize session state to store previous entries
    if 'previous_entries' not in st.session_state:
        st.session_state.previous_entries = []

    # Initialize form for automatic submission
    with st.form(key='process_form'):
        # Text input boxes with placeholders
        h_number = st.text_input("Scan your H number", value="", placeholder="Scan your H number")
        order_number = st.text_input("Scan the Planned Order Number", value="", placeholder="Scan the Planned Order Number")
        line_id = st.text_input("Scan the Line ID", value="", placeholder="Scan the Line ID")

        # User input box for job quantity
        job_quantity = st.number_input("Scan the Job Quantity", min_value=1, step=1, value=1)

        serial_number = st.text_input("Scan the Product Serial Number", value="", placeholder="Scan the Product Serial Number")

        # Form submit button
        submitted = st.form_submit_button("Submit")

        # Store entries if form is submitted and all fields are filled
        if submitted and h_number and order_number and line_id and serial_number:
            store_entry(h_number, order_number, line_id, job_quantity, serial_number)
            st.success("Entry submitted successfully!")

            # Refresh the form
            st.experimental_rerun()

    # Display table of previous entries for serial numbers
    display_previous_entries()

def store_entry(h_number, order_number, line_id, job_quantity, serial_number):
    st.session_state.previous_entries.append({"H Number": h_number, "Order Number": order_number, "Line ID": line_id, "Job Quantity": job_quantity, "Serial Number": serial_number})

def display_previous_entries():
    if len(st.session_state.previous_entries) > 0:
        st.subheader("Previous Entries for Serial Numbers")
        df = pd.DataFrame(st.session_state.previous_entries)
        st.table(df)

if __name__ == "__main__":
    main()