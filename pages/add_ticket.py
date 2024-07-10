import streamlit as st
import pandas as pd
from utils.db_operations import load_tickets, save_tickets, load_units

# Function to display the Add Ticket page
def add_ticket_page():
    st.title("Add Ticket")

    units = load_units('data/units.csv')
    tickets = load_tickets('data/tickets.csv')

    unit_id = st.selectbox("Select Unit", units['Unit ID'])
    
    with st.form(key='ticket_form'):
        ticket_data = {}
        ticket_data['Unit ID'] = unit_id
        ticket_data['Check Date'] = st.date_input("Check Date")
        ticket_data['Issue'] = st.text_input("Issue")
        ticket_data['Part'] = st.text_input("Part")
        ticket_data['Repair Status'] = st.selectbox("Repair Status", ["Complete", "Pending"])
        ticket_data['Date Repaired'] = st.date_input("Date Repaired")
        ticket_data['Cost'] = st.number_input("Cost", min_value=0.0, format="%.2f")
        
        submit_button = st.form_submit_button(label='Save Ticket')

    if submit_button:
        tickets = tickets.append(ticket_data, ignore_index=True)
        save_tickets('data/tickets.csv', tickets)
        st.success('Ticket information saved successfully!')

