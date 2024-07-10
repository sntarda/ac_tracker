import streamlit as st

def display_page():
    st.title("Building 1055 Units")
    unit_list = ["RTU 1", "RTU 2", "RTU 3"]  # Example units, replace with actual data fetching logic
    
    for unit in unit_list:
        if st.button(unit):
            st.session_state['selected_unit'] = unit
            st.experimental_rerun()
    
    if 'selected_unit' in st.session_state:
        display_unit_details(st.session_state['selected_unit'])

def display_unit_details(unit):
    st.subheader(f"Details for {unit}")
    st.write("Location: [Insert Location]")
    st.write("Tenant: [Insert Tenant]")
    st.write("Manufacturer: Carrier")
    st.write("Model Number: 65465464")
    st.write("Serial Number: 15663489")
    st.write("Tonnage: 5")
    st.write("SEER: [Insert SEER]")
    st.write("Heat: [Insert Heat]")
    st.write("Status: Operational")
    st.write("Last Service: [Insert Date]")
    st.write("Tickets:")
    ticket_data = [["2023-07-01", "Issue 1", "Part 1", "Complete", "2023-07-02", "$200"]]
    st.table(ticket_data)
    if st.button("Upload Image"):
        st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])
    if st.button("Upload Document"):
        st.file_uploader("Choose a file", type=["pdf", "docx"])
