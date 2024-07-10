import streamlit as st
import streamlit_authenticator as stauth

# Example credentials dictionary
credentials = {
    'usernames': {
        'user1': {
            'name': 'User One',
            'password': stauth.Hasher(['password']).generate()[0]
        },
        'user2': {
            'name': 'User Two',
            'password': stauth.Hasher(['password2']).generate()[0]
        }
    }
}

authenticator = stauth.Authenticate(credentials, 'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)

def login():
    name, authentication_status, username = authenticator.login('Login', 'main')
    if authentication_status:
        st.session_state['authenticated'] = True
        return True
    elif authentication_status == False:
        st.error('Username/password is incorrect')
        return False
    elif authentication_status == None:
        st.warning('Please enter your username and password')
        return False

def logout():
    authenticator.logout('Logout', 'sidebar')
    st.session_state['authenticated'] = False
