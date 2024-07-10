import streamlit as st
from models.database import session, Unit
from datetime import date

def show():
    st.title("Add/Edit Unit")
    unit_id = st.text_input("Unit ID (leave blank to add new)")
    facility = st.text_input("Facility")
    tenant = st.text_input("Tenant")
    manufacturer = st.text_input("Manufacturer")
    model_number = st.text_input("Model Number")
    serial_number = st.text_input("Serial Number")
    tonnage = st.number_input("Tonnage", min_value=0.0, step=0.1)
    seer = st.number_input("Seer", min_value=0.0, step=0.1)
    heat = st.text_input("Heat")
    status = st.selectbox("Status", ["Operational", "Maintenance Required", "Faulty", "Not Cooling", "Off", "Standby", "Due for Routine Service", "Decommissioned", "Testing"])
    last_service = st.date_input("Last Service", value=date.today())

    if st.button("Save Unit"):
        if unit_id:
            unit = session.query(Unit).filter(Unit.id == unit_id).first()
            unit.facility = facility
            unit.tenant = tenant
            unit.manufacturer = manufacturer
            unit.model_number = model_number
            unit.serial_number = serial_number
            unit.tonnage = tonnage
            unit.seer = seer
            unit.heat = heat
            unit.status = status
            unit.last_service = last_service
        else:
            new_unit = Unit(
                facility=facility,
                tenant=tenant,
                manufacturer=manufacturer,
                model_number=model_number,
                serial_number=serial_number,
                tonnage=tonnage,
                seer=seer,
                heat=heat,
                status=status,
                last_service=last_service,
            )
            session.add(new_unit)
        session.commit()
        st.success("Unit saved successfully!")

