import streamlit as st
import pandas as pd
from utils.db_operations import load_units, save_units

# Function to display the Add/Edit Unit page
def add_edit_unit_page():
    st.title("Add/Edit Unit")

    units = load_units('data/units.csv')

    unit_id = st.selectbox("Select Unit to Edit (or select 'New Unit' to add a new unit)", ['New Unit'] + list(units['Unit ID']))

    if unit_id == 'New Unit':
        new_unit = True
        unit_data = {}
    else:
        new_unit = False
        unit_data = units[units['Unit ID'] == unit_id].to_dict('records')[0]

    with st.form(key='unit_form'):
        unit_data['Unit ID'] = st.text_input("Unit ID", unit_data.get('Unit ID', ''))
        unit_data['Manufacturer'] = st.text_input("Manufacturer", unit_data.get('Manufacturer', ''))
        unit_data['Model Number'] = st.text_input("Model Number", unit_data.get('Model Number', ''))
        unit_data['Serial Number'] = st.text_input("Serial Number", unit_data.get('Serial Number', ''))
        unit_data['Tonnage'] = st.number_input("Tonnage", unit_data.get('Tonnage', 0), format="%d")
        unit_data['Seer'] = st.text_input("Seer", unit_data.get('Seer', ''))
        unit_data['Heat'] = st.text_input("Heat", unit_data.get('Heat', ''))
        
        submit_button = st.form_submit_button(label='Save')

    if submit_button:
        if new_unit:
            units = units.append(unit_data, ignore_index=True)
        else:
            units.update(unit_data)
        
        save_units('data/units.csv', units)
        st.success('Unit information saved successfully!')

