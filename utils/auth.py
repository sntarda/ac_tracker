from streamlit_authenticator import Authenticate

credentials = {
    'usernames': {
        'admin': {'password': 'password'}
    }
}

authenticator = Authenticate(
    credentials=credentials,
    cookie_name="ac_tracker",
    key="some_random_key",
    cookie_expiry_days=1,
)
