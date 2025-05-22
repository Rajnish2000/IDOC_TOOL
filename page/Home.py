import streamlit as st
from PIL import Image
import base64

# def set_background(image_path):
#     with open(image_path, "rb") as f:
#         base64_img = base64.b64encode(f.read()).decode()
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url("data:image/png;base64,{base64_img}");
#             background-size: cover;
#             background-attachment: fixed;
#         }}
#         .big-font {{
#             font-size: 30px !important;
#             color: #013A63;
#         }}
#         .subtle-box {{
#             background-color: rgba(255,255,255,0.85);
#             padding: 2rem;
#             border-radius: 1rem;
#             box-shadow: 0px 4px 16px rgba(0, 0, 0, 0.15);
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# Custom background CSS (Optional)
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

 
    
def app():
    # st.set_page_config(page_title="Home")
    # if 'user' not in st.session_state:
    #     st.warning("You must log in to access this page.")
    #     # st.switch_page("Login.py")
    #     print(st.session_state)
    #     # st.query_params = {"page": "Login"}
    #     # st.rerun()
    # else:
        # st.title("🏠 Home Page")
        # st.success(f"Welcome, {st.session_state['user']['email']}!")
        
        st.title('Welcome to :violet[I-DOC-TOOL] 📃')
        # Optional: Add a light background
        set_background("assets/light_background_1.png")  # Optional background image
        
        # Header Section
        # st.markdown("<h1 class='big-font'>📄 I-Doc-Tool</h1>", unsafe_allow_html=True)
        st.markdown("### Your Intelligent Document Companion")

        # Hero Section
        col1, col2 = st.columns([1.2, 1])

        with col1:
            st.markdown("""
            <div class="subtle-box">
                <h2>🚀 Supercharge your documentation workflow!</h2>
                <p style='font-size:17px;'>I-Doc-Tool helps you manage, analyze, and extract value from your documents in seconds with powerful AI tools.</p>
                <ul>
                    <li>🔍 Smart Search Across Docs</li>
                    <li>📁 Multi-format Uploads (PDF, DOCX, Text)</li>
                    <li>✏️ Annotate and Highlight Text</li>
                    <li>🔐 Secure Cloud-based Storage</li>
                    <li>⚙️ Role-based Access & Sessions</li>
                </ul>
                <br>
                <a href="/Login" target="_self">
                    <button style='font-size:18px;padding:12px 30px;border-radius:10px;background:#003566;color:white;border:none;'>🔐 Get Started</button>
                </a>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            image = Image.open("assets/idoc_banner.png")
            image1 = Image.open("assets/light_background.png")
            st.image(image, use_container_width=True)
            st.image(image1, use_container_width=True)

        # Feature Cards
        st.markdown("---")
        st.markdown("## ✨ Key Features")

        f1, f2, f3 = st.columns(3)
        with f1:
            st.markdown("""
            <div class="subtle-box">
            <h4>📄 Upload & Organize</h4>
            <p>Easily upload and manage documents in a structured dashboard.</p>
            </div>
            """, unsafe_allow_html=True)
        with f2:
            st.markdown("""
            <div class="subtle-box">
            <h4>🔎 AI-powered Search</h4>
            <p>Instantly search across documents using semantic AI search tools.</p>
            </div>
            """, unsafe_allow_html=True)
        with f3:
            st.markdown("""
            <div class="subtle-box">
            <h4>🧠 Smart Summaries</h4>
            <p>Summarize long files with AI and extract meaningful insights.</p>
            </div>
            """, unsafe_allow_html=True)

        # How It Works
        st.markdown("---")
        st.markdown("## 🧰 How It Works")

        st.markdown("""
        <div class="subtle-box">
        <ol style='font-size:17px;'>
            <li>Sign Up / Log In to your secure account</li>
            <li>Upload Documents in PDF, DOCX, or Text format</li>
            <li>Use AI to Search, Annotate, and Summarize</li>
            <li>Collaborate with team members and export insights</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)

        # Testimonials
        st.markdown("---")
        st.markdown("## 💬 What Users Say")
        c1, c2 = st.columns(2)

        with c1:
            st.markdown("""
            <div class="subtle-box">
            <em>“I-Doc-Tool saved me hours every week! The AI search is incredibly accurate.”</em><br><strong>– Aayush, Legal Analyst</strong>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown("""
            <div class="subtle-box">
            <em>“Exactly what I needed for my thesis work. Smart summaries are 🔥”</em><br><strong>– Priya, Research Scholar</strong>
            </div>
            """, unsafe_allow_html=True)

        # Final CTA
        st.markdown("---")
        st.markdown("## 🎯 Ready to Get Started?")
        st.markdown("Click below to login and begin your intelligent document journey!")

        st.markdown("""
        <a href="/Login" target="_self">
            <button style='font-size:18px;padding:14px 40px;border-radius:10px;background:#1d3557;color:white;border:none;'>👉 Log In Now</button>
        </a>
        """, unsafe_allow_html=True)