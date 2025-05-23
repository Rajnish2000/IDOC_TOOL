import firebase_auth as fa
import streamlit as st

def load_css():
    st.markdown("""
        <style>
        /* Background gradient */
        body, .stApp {
            background: linear-gradient(135deg, #E0EAFC, #CFDEF3);
            font-family: 'Segoe UI', sans-serif;
        }

        /* Centering form */
        .login-container {
            max-width: 400px;
            margin: 5% auto;
            background-color: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }

        /* Stylish button */
        .stButton button {
            background-color: #4A90E2;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1.2rem;
            font-size: 1rem;
            font-weight: bold;
            margin-top: 10px;
        }

        .stButton button:hover {
            background-color: #357ABD;
        }

        /* Link styling */
        .login-links {
            margin-top: 1rem;
            text-align: center;
            font-size: 0.9rem;
        }

        .login-links a {
            color: #4A90E2;
            text-decoration: none;
            margin: 0 8px;
        }

        .login-links a:hover {
            text-decoration: underline;
        }

        .social-buttons {
            display: flex;
            justify-content: space-between;
            margin-top: 1.5rem;
        }

        .social-buttons button {
            flex: 1;
            margin: 0 0.5rem;
            background-color: #f5f5f5;
            color: #333;
            border-radius: 6px;
        }

        </style>
    """, unsafe_allow_html=True)




def login():
    st.title('Welcome to :violet[I-DOC] :sunglasses:')
    with st.container():
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.markdown("#### Login to your account")    
    
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

        st.markdown("""
        </div>
        """, unsafe_allow_html=True)