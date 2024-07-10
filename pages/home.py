import streamlit as st

# Function to display the home page
def home_page():
    st.title("Company Information")
    
    # Display company information
    st.write("**Company Name:** Your Company Name")
    st.write("**Address:** 1234 Main St, Anytown, TX 12345")
    st.write("**Phone Number:** (123) 456-7890")
    
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

