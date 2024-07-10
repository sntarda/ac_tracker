import streamlit as st
from models.database import session, Unit

def show():
    st.title("Building 1055")
    units = session.query(Unit).filter(Unit.facility == "1055 Address").all()
    
    for unit in units:
        if st.button(f"RTU {unit.id}"):
            st.write(f"Details for RTU {unit.id}")
            st.write(f"Tenant: {unit.tenant}")
            st.write(f"Manufacturer: {unit.manufacturer}")
            st.write(f"Model Number: {unit.model_number}")
            st.write(f"Serial Number: {unit.serial_number}")
            st.write(f"Tonnage: {unit.tonnage}")
            st.write(f"Seer: {unit.seer}")
            st.write(f"Heat: {unit.heat}")
            st.write(f"Status: {unit.status}")
            st.write(f"Last Service: {unit.last_service}")

