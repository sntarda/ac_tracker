import streamlit as st
from models.database import session, Ticket, Unit
from datetime import date

def show():
    st.title("Add Ticket")
    
    # Fetching unit IDs from the database
    units = session.query(Unit).all()
    unit_options = {unit.id: f"RTU {unit.id} ({unit.facility})" for unit in units}
    
    unit_id = st.selectbox("Unit", options=unit_options.keys(), format_func=lambda x: unit_options[x])
    issue = st.text_area("Issue")
    part = st.text_input("Part")
    repair_status = st.selectbox("Repair Status", ["Complete", "Pending"])
    check_date = st.date_input("Check Date", value=date.today())
    date_repaired = st.date_input("Date Repaired", value=date.today())
    cost = st.number_input("Cost", min_value=0.0, step=0.1)

    if st.button("Save Ticket"):
        new_ticket = Ticket(
            unit_id=unit_id,
            issue=issue,
            part=part,
            repair_status=repair_status,
            check_date=check_date,
            date_repaired=date_repaired,
            cost=cost
        )
        session.add(new_ticket)
        session.commit()
        st.success("Ticket saved successfully!")
