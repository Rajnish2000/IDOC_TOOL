import firebase_auth as fa
import streamlit as st

def login():
    st.title('Login to :violet[I-DOC] :sunglasses:')
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            user = fa.auth.sign_in_with_email_and_password(email, password)
            st.session_state['user'] = user
            st.success("You Logged in!")
            st.balloons()
            st.rerun()
        except Exception as e:
            st.error(f"Login failed: {e}")
