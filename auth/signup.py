import streamlit as st
from firebase_auth import auth, db


def signup():
    st.title('Sign Up to :violet[I-DOC] :sunglasses:')
    with st.form("signup_form"):
        # new_username = st.text_input("Username")
        new_email = st.text_input("Email")
        new_password = st.text_input("Password", type="password")
        confirm = st.text_input("Confirm Password", type="password")

        if st.form_submit_button("Register"):
            try:
                if new_password == confirm:
                    user = auth.create_user_with_email_and_password(new_email, new_password)
                    uid = user['localId']
                    db.collection("users").document(uid).set({"email": new_email})
                    
                    # adding details for the profile page also.
                    profile_ref = db.collection('users').document(uid).collection("profile").document("info")
                    
                    profile_data = profile_ref.get().to_dict() or {}
                    profile_ref.set({
                        "name": '',
                        "email": new_email,
                        "notify": False,
                        "password": new_password if new_password else profile_data.get("password")
                    })
                    st.success("Account created. Please log in.")
                    st.balloons()
                else:
                    st.error("Passwords do not match")
            except Exception as e:
                st.error(f"Error: {e}")