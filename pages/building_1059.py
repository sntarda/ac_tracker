import streamlit as st
from utils.db_operations import load_units

# Function to display the Building 1059 page
def building_1059_page():
    st.title("Building 1059")

    units = load_units('data/units.csv')
    building_units = units[units['Facility'] == '1059 S Sherman']

    if building_units.empty:
        st.write("No units found for Building 1059.")
    else:
        for index, unit in building_units.iterrows():
            if st.button(unit['Unit ID']):
                st.session_state.selected_unit = unit['Unit ID']
                st.session_state.page = 'unit_detail'

# Display the selected unit details if available
if 'selected_unit' in st.session_state:
    from pages.unit_detail import unit_detail_page
    unit_detail_page(st.session_state.selected_unit)
