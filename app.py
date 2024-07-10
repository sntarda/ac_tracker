import streamlit as st
from utils.auth import authenticate_user
from pages.login import login_page
from pages.home import home_page
from pages.add_edit_unit import add_edit_unit_page
from pages.add_ticket import add_ticket_page
from pages.building_1001 import building_1001_page
from pages.building_1055 import building_1055_page
from pages.building_1057 import building_1057_page
from pages.building_1059 import building_1059_page
from pages.unit_detail import unit_detail_page
from pages.upload_image import upload_image_page
from pages.upload_document import upload_document_page
from pages.view_tickets import view_tickets_page

# Function to display the main menu
def display_menu():
    st.sidebar.title("Main Menu")
    st.sidebar.button("Logout", key="logout")
    st.sidebar.markdown("---")
    st.sidebar.button("Home/Dashboard", key="home")
    st.sidebar.button("Add/Edit Unit", key="add_edit_unit")
    st.sidebar.button("Add Ticket", key="add_ticket")
    st.sidebar.button("Building 1001", key="building_1001")
    st.sidebar.button("Building 1055", key="building_1055")
    st.sidebar.button("Building 1057", key="building_1057")
    st.sidebar.button("Building 1059", key="building_1059")

# Main function to run the app
def main():
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False

    if st.session_state.authenticated:
        display_menu()
        page = st.sidebar.radio("Navigation", ["Home/Dashboard", "Add/Edit Unit", "Add Ticket",
                                               "Building 1001", "Building 1055", "Building 1057", "Building 1059"],
                                key="navigation")

        if page == "Home/Dashboard":
            home_page()
        elif page == "Add/Edit Unit":
            add_edit_unit_page()
        elif page == "Add Ticket":
            add_ticket_page()
        elif page == "Building 1001":
            building_1001_page()
        elif page == "Building 1055":
            building_1055_page()
        elif page == "Building 1057":
            building_1057_page()
        elif page == "Building 1059":
            building_1059_page()
        elif page == "unit_detail":
            unit_detail_page()
        elif page == "upload_image":
            upload_image_page()
        elif page == "upload_document":
            upload_document_page()
        elif page == "view_tickets":
            view_tickets_page()
    else:
        login_page()

if __name__ == "__main__":
    main()
