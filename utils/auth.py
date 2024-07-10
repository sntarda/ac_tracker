import streamlit_authenticator as stauth

# Example credentials dictionary with hashed passwords
hashed_passwords = stauth.Hasher(['password']).generate()

credentials = {
    'usernames': {
        'admin': {
            'name': 'Admin User',
            'password': hashed_passwords[0]
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
