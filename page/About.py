import streamlit as st
from PIL import Image
import streamlit as st
from utils.background import set_background

def app():
    # st.subheader('share their valuable thoughts with the world')
    # st.set_page_config(page_title="About")
    # st.set_page_config(page_title="About - I-Doc-Tool", layout="wide")
    st.title("📘 About :violet[I-DOC-TOOL]")
    set_background("assets/light_background_1.png")
    st.markdown("### Your Smart Document Assistant")

    # Hero section
    st.image("assets/idoc_banner.png", use_container_width =True)

    st.markdown("""
    Welcome to **I-Doc-Tool**, a modern, AI-powered platform built to **simplify, manage, and automate** your documentation workflows.

    Our mission is to **empower individuals and teams** to collaborate, extract insights, and securely manage documents — all from a unified interface.
    """)

    # Feature Highlights
    st.markdown("---")
    st.markdown("## 🚀 Why Use I-Doc-Tool?")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🔍 Smart Search")
        st.markdown("Find information instantly across large document sets with AI-powered semantic search.")

    with col2:
        st.markdown("### 📄 Multi-Format Support")
        st.markdown("Upload, view, and edit PDFs, Word files, images, and text formats seamlessly.")

    with col3:
        st.markdown("### 🔐 Secure & Private")
        st.markdown("All your data is encrypted and protected with industry-grade security using Firebase.")

    # Use Cases
    st.markdown("---")
    st.markdown("## 💼 Who Is It For?")
    st.markdown("""
    - ✅ **Students**: Organize notes and academic materials with ease  
    - ✅ **Lawyers**: Analyze contracts and legal documents faster  
    - ✅ **Businesses**: Automate report generation and document workflows  
    - ✅ **Researchers**: Extract and annotate findings from scientific papers  
    """)

    # Tech stack section
    st.markdown("---")
    st.markdown("## 🛠️ Built With Modern Tech")
    st.markdown("""
    - **Frontend**: [Streamlit](https://streamlit.io) with responsive layout  
    - **Backend**: Python, Firebase (Auth + Firestore), Tesseract OCR, OpenCV.  
    - **Authentication**: Firebase Auth and session management  
    - **AI Support**: Integrated with Deep based OCR for exact Extraction (optional)  
    """)

    # Vision
    st.markdown("---")
    st.markdown("## 🌟 Our Vision")
    st.info("We envision a world where documents are not just stored — they are understood, connected, and actionable.")

    # Footer / Help
    st.markdown("---")
    st.markdown("## 🤝 Need Help?")
    st.markdown("If you have questions or suggestions, reach out at [support@idoc-tool.com](mailto:support@idoc-tool.com) or use the **Contact** page.")

    st.success("Thank you for choosing I-Doc-Tool — your intelligent document companion!")
