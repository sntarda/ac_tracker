import streamlit as st
from utils.db_operations import load_tickets

# Function to display the tickets for a specific unit
def view_tickets_page():
    st.title("View Tickets")

    unit_id = st.session_state.get('selected_unit')
    if unit_id is None:
        st.error("No unit selected.")
        return

    tickets = load_tickets('data/tickets.csv')
    unit_tickets = tickets[tickets['Unit ID'] == unit_id]

    if unit_tickets.empty:
        st.write("No tickets found for this unit.")
    else:
        st.dataframe(unit_tickets)

    if st.button("Back to Unit Details"):
        st.session_state.page = 'unit_detail'
        st.session_state.selected_unit = unit_id

