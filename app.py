import streamlit as st
from utils.auth import authenticator
from pages import add_edit_unit, add_ticket, building_1001, building_1055, building_1057, building_1059

# Authentication
name, authentication_status, username = authenticator.login('Login')

if authentication_status:
    st.sidebar.title(f"Welcome {name}")
    menu = st.sidebar.radio("Main Menu", ["Home/Dashboard", "Add/Edit Unit", "Add Ticket", "Building 1001", "Building 1055", "Building 1057", "Building 1059"])

    if menu == "Home/Dashboard":
        st.title("Home/Dashboard")
        st.write("Company Information")
        st.write("Company Name: AC Tracker Inc.")
        st.write("Address: 123 Main St")
        st.write("Phone: 555-555-5555")
    elif menu == "Add/Edit Unit":
        add_edit_unit.show()
    elif menu == "Add Ticket":
        add_ticket.show()
    elif menu == "Building 1001":
        building_1001.show()
    elif menu == "Building 1055":
        building_1055.show()
    elif menu == "Building 1057":
        building_1057.show()
    elif menu == "Building 1059":
        building_1059.show()

    st.sidebar.button("Logout", on_click=authenticator.logout)

elif authentication_status == False:
    st.error('Username/password is incorrect')

elif authentication_status == None:
    st.warning('Please enter your username and password')
