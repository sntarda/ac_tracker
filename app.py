import streamlit as st
from utils.auth import login, logout
from pages import add_edit_unit, add_ticket, building_1001, building_1055, building_1057, building_1059

st.set_page_config(page_title="AC Unit Tracker", layout="wide")

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if not st.session_state['authenticated']:
    st.session_state['authenticated'] = login()

if st.session_state['authenticated']:
    with st.sidebar:
        st.sidebar.title("Main Menu")
        menu = st.sidebar.radio("Navigation", ["Home/Dashboard", "Add/Edit Unit", "Add Ticket", "Building 1001", "Building 1055", "Building 1057", "Building 1059", "Logout"])

    if menu == "Logout":
        logout()
    elif menu == "Home/Dashboard":
        st.title("Home Page")
        st.write("Company Information: [Insert details here]")
    elif menu == "Add/Edit Unit":
        add_edit_unit.display_page()
    elif menu == "Add Ticket":
        add_ticket.display_page()
    elif menu == "Building 1001":
        building_1001.display_page()
    elif menu == "Building 1055":
        building_1055.display_page()
    elif menu == "Building 1057":
        building_1057.display_page()
    elif menu == "Building 1059":
        building_1059.display_page()
else:
    st.write("Please login to access the application.")
