import streamlit as st
import base64

def set_background(image_path):
    with open(image_path, "rb") as f:
        base64_img = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{base64_img}");
            background-size: cover;
            background-attachment: fixed;
            font-family: 'Segoe UI', sans-serif;
        }}
        .big-font {{
            font-size: 40px !important;
            color: #012a4a;
            font-weight: bold;
        }}
        .subtle-box {{
            background-color: rgba(255,255,255,0.95);
            padding: 2.5rem;
            border-radius: 1.2rem;
            box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease-in-out;
        }}
        ul li {{
            margin: 0.4rem 0;
            font-size: 17px;
        }}
        button:hover {{
            background-color: #ffc300 !important;
            color: #000 !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
