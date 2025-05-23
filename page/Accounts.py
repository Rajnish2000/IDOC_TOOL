import streamlit as st
from firebase_auth import auth, db
from firebase_auth import firebase_web_config
import requests

def update_password(id_token, new_password, api_key):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:update?key={api_key}"
    payload = {
        "idToken": id_token,
        "password": new_password,
        "returnSecureToken": True
    }
    response = requests.post(url, json=payload)
    return response.json()

def app(user):
    uid = user['localId']
    print('uid : ',uid)
    
    profile_ref = db.collection('users').document(uid).collection("profile").document("info")
    prefs_ref = db.collection('users').document(uid).collection("preferences").document("settings")    
    
    # Load profile & preferences from Firestore
    profile_data = profile_ref.get().to_dict() or {}
    prefs_data = prefs_ref.get().to_dict() or {}
    print('profile_ref: ',profile_ref)
    print('prefs_ref: ',prefs_ref)
    print('profile_data: ',profile_data)
    print('pref_data: ',prefs_data)
    # Page Title
    st.markdown("""
        <h1 style='font-size: 36px; color: #1d3557;'>👤 My Account</h1>
        <p style='font-size:18px;color:#457b9d;'>Manage your profile, settings, and preferences</p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Layout Columns
    col1, col2 = st.columns([1, 2])

    # Profile Section
    with col1:
        st.image("assets/user_avatar.png", width=150)
        st.markdown(f"""
            <h5 style='color:#6c757d;'>🧔 User </h5>
            <h3 style='color:#1d3557;'>{profile_data.get("name")}</h3>
        """, unsafe_allow_html=True)

    # Settings Section
    with col2:
        st.markdown("""
            <div style='background-color: #f1faee; padding: 20px; border-radius: 10px;'>
            <h4 style='color:#1d3557;'>🔧 Account Settings</h4>
        """, unsafe_allow_html=True)

        name = st.text_input("Full Name", value=profile_data.get("name"))
        email = st.text_input("Email", value=profile_data.get("email"))
        password = st.text_input("Change Password", type="password",value=profile_data.get("password"))
        notify = st.checkbox("Email me about updates", value=profile_data.get("notify", True))

        if st.button("💾 Save Changes"):
            profile_ref.set({
                "name": name,
                "email": email,
                "notify": notify,
                "password": password if password else profile_data.get("password")
            })
            st.balloons()
            try:
                if password:
                    auth.refresh(user['refreshToken']) 
                    auth.update_profile(user['idToken'], display_name=name)
                    update_password(user['idToken'], password, firebase_web_config["apiKey"])
                    st.success("✅ Profile and password updated successfully!")
                else:
                    st.success("✅ Profile updated successfully!")
            except Exception as e:
                st.error(f"Failed to update password: {e}")

        st.markdown("</div>", unsafe_allow_html=True)

    # Preferences
    st.markdown("---")
    st.markdown("""
        <h4 style='color:#1d3557;'>⚙️ Preferences</h4>
        <p style='color:#6c757d;'>Customize how you use I-Doc-Tool</p>
    """, unsafe_allow_html=True)

    pref_col1, pref_col2 = st.columns(2)

    with pref_col1:
        theme = st.selectbox("App Theme", ["Light", "Dark", "System Default"])
        lang = st.selectbox("Language", ["English", "Hindi", "Spanish"])

    with pref_col2:
        timezone = st.selectbox("Time Zone", ["UTC", "IST", "EST", "PST"])

    if st.button("✅ Update Preferences"):
        prefs_ref.set({
            "theme": theme,
            "language": lang,
            "timezone": timezone
        })
        st.success("Preferences saved!")