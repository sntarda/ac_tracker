import streamlit as st
from utils.db_operations import load_units, load_tickets
import pandas as pd

# Function to display the Unit Detail page
def unit_detail_page(unit_id):
    st.title(f"Unit Details: {unit_id}")

    units = load_units('data/units.csv')
    unit = units[units['Unit ID'] == unit_id].iloc[0]

    # Display unit location and details
    st.subheader("Unit Location")
    st.write(f"**Facility:** {unit['Facility']}")
    st.write(f"**Tenant:** {unit['Tenant']}")

    st.subheader("Unit Details")
    st.write(f"**Manufacturer:** {unit['Manufacturer']}")
    st.write(f"**Model Number:** {unit['Model Number']}")
    st.write(f"**Serial Number:** {unit['Serial Number']}")
    st.write(f"**Tonnage:** {unit['Tonnage']}")
    st.write(f"**Seer:** {unit['Seer']}")
    st.write(f"**Heat:** {unit['Heat']}")

    # Image upload button
    st.subheader("Images")
    if st.button("Upload Image"):
        st.session_state.page = 'upload_image'
    
    # Maintenance status
    st.subheader("Unit Maintenance")
    status_options = ["Operational", "Maintenance Required", "Faulty", "Not Cooling", "Off", "Standby", "Due for Routine Service", "Decommissioned", "Testing"]
    st.write(f"**Status:** {st.selectbox('Status', status_options, index=status_options.index(unit.get('Status', 'Operational')))}")
    st.write(f"**Last Service:** {st.date_input('Last Service', pd.to_datetime(unit.get('Last Service', pd.Timestamp.today())))}")

    # Document upload button
    st.subheader("Documents")
    if st.button("Upload Document"):
        st.session_state.page = 'upload_document'

    # Display associated tickets
    st.subheader("Tickets")
    tickets = load_tickets('data/tickets.csv')
    unit_tickets = tickets[tickets['Unit ID'] == unit_id]
    st.dataframe(unit_tickets)

    if st.button("Add Ticket"):
        st.session_state.page = 'add_ticket'


