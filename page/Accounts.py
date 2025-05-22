import streamlit as st

def app():
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
        st.markdown("""
            <h5 style='color:#6c757d;'>🧔 User </h5>
            <h3 style='color:#1d3557;'>Raj Singh</h3>
        """, unsafe_allow_html=True)

    # Settings Section
    with col2:
        st.markdown("""
            <div style='background-color: #f1faee; padding: 20px; border-radius: 10px;'>
            <h4 style='color:#1d3557;'>🔧 Account Settings</h4>
        """, unsafe_allow_html=True)

        name = st.text_input("Full Name", value="Raj singh")
        email = st.text_input("Email", value="raj@gmail.com")
        password = st.text_input("Change Password", type="password")
        notify = st.checkbox("Email me about updates", value=True)

        if st.button("💾 Save Changes"):
            st.success("✅ Profile updated successfully!")

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
        # autosave = st.radio("Auto-save documents", ["Yes", "No"])

    if st.button("✅ Update Preferences"):
        st.success("Preferences saved!")