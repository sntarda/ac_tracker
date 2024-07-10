import streamlit as st

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "password":  # Replace with your authentication logic
            st.session_state['authenticated'] = True
            return True
        else:
            st.error("Invalid credentials")
    return False

def logout():
    st.session_state['authenticated'] = False
    st.experimental_rerun()

def check_authentication():
    return st.session_state['authenticated']
