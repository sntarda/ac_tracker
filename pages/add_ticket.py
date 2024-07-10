import streamlit as st

def display_page():
    st.title("Add Ticket")
    unit_id = st.text_input("Unit ID")
    issue = st.text_input("Issue")
    part = st.text_input("Part")
    repair_status = st.selectbox("Repair Status", ["Complete", "Pending"])
    date_repaired = st.date_input("Date Repaired")
    cost = st.number_input("Cost", min_value=0.0, step=0.1)
    
    if st.button("Save"):
        st.success("Ticket details saved successfully")
