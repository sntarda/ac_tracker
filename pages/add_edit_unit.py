import streamlit as st

def display_page():
    st.title("Add/Edit Unit")
    unit_id = st.text_input("Unit ID")
    location = st.text_input("Location")
    manufacturer = st.text_input("Manufacturer")
    model_number = st.text_input("Model Number")
    serial_number = st.text_input("Serial Number")
    tonnage = st.number_input("Tonnage", min_value=0.0, step=0.1)
    seer = st.text_input("SEER")
    heat = st.text_input("Heat")
    
    if st.button("Save"):
        st.success("Unit details saved successfully")
