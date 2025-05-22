import streamlit as st

def app():
    # st.set_page_config(page_title="Contact")
    st.title("📬 Contact Us")

    # Inject styles and layout
    st.markdown("""
        <style>
        .contact-container {
            max-width: 600px;
            margin: auto;
            padding: 2rem;
            background-color: white;
            border-radius: 20px;
            box-shadow: 0 12px 32px rgba(0,0,0,0.1);
            font-family: 'Segoe UI', sans-serif;
        }
        input, textarea {
            width: 100%;
            padding: 0.75rem;
            margin-bottom: 1.2rem;
            border: 2px solid #ccc;
            border-radius: 10px;
            font-size: 1rem;
        }
        .send-button {
            background-color: #1e3c72;
            color: white;
            padding: 1rem;
            font-size: 1.1rem;
            font-weight: bold;
            border: none;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            cursor: pointer;
            transition: background 0.3s ease;
            width: 100%;
        }
        .send-button:hover {
            background-color: #2952a3;
        }
        .send-button svg {
            stroke: white;
        }
        .contact-info {
        text-align: center;
        margin-top: 3rem;
        color: #1e3c72;
        font-weight: 600;
        font-size: 1rem;
        user-select: none;
    }
    .contact-info a {
        color: #1e3c72;
        text-decoration: none;
        margin: 0 0.6rem;
        transition: color 0.3s ease;
    }
    .contact-info a:hover {
        color: #2952a3;
    }
    /* Responsive */
    @media (max-width: 640px) {
        .card {
            margin: 1rem;
            padding: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # Form UI
    st.markdown('<div class="contact-container">', unsafe_allow_html=True)
    st.markdown("## 📬 Contact Us")
    st.markdown("Have any questions? Fill out the form below and we’ll get back to you.")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    # Create the custom HTML button
    send_button_html = """
        <form action="" method="post">
            <button class="send-button" name="submit_btn">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" stroke="currentColor"
                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                    class="feather feather-send" viewBox="0 0 24 24">
                <line x1="22" y1="2" x2="11" y2="13"></line>
                <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
                </svg>
                Send
            </button>
        </form>
    """
    st.markdown(send_button_html, unsafe_allow_html=True)

    # Detect the "submit" manually
    if st.session_state.get("submitted") is None:
        st.session_state["submitted"] = False

    # Use query param or state as workaround (simulate POST)
    query_params = st.query_params
    if "submit_btn" in query_params:
        st.session_state["submitted"] = True

    # Handle logic
    if st.session_state["submitted"]:
        if not name.strip() or not email.strip() or not message.strip():
            st.error("Please fill in all the fields.")
        else:
            st.success("🎉 Thank you for contacting us! We'll respond shortly.")
            st.session_state["submitted"] = False  # reset after success

    st.markdown("</div>", unsafe_allow_html=True)
    
    # Contact info with icons and social links
    st.markdown(
        """
        <div class="contact-info">
            <p>Or reach us at: <a href="mailto:contact@idoctool.com">contact@idoctool.com</a></p>
            <p>
            <a href="https://twitter.com" target="_blank" title="Twitter" aria-label="Twitter">🐦</a> 
            <a href="https://linkedin.com" target="_blank" title="LinkedIn" aria-label="LinkedIn">🔗</a> 
            <a href="https://facebook.com" target="_blank" title="Facebook" aria-label="Facebook">📘</a>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )