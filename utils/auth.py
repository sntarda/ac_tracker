import streamlit_authenticator as stauth

# Example credentials dictionary
credentials = {
    'usernames': {
        'admin': {
            'name': 'Admin User',
            'password': stauth.Hasher(['password']).generate()  # Hash the password
        }
    }
}

cookie = {
    'expiry_days': 30,
    'key': 'some_random_key',
    'name': 'ac_tracker_cookie'
}

preauthorized = {
    'emails': ['admin@domain.com']
}

# Initialize the authenticator
authenticator = stauth.Authenticate(
    credentials,
    cookie['name'],
    cookie['key'],
    cookie['expiry_days'],
    preauthorized
)
