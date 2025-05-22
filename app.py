import streamlit as st
# from auth.login import login
st.set_page_config(page_title="I-DOC TOOL")
from streamlit_option_menu import option_menu

import page.About as about
import page.Accounts as account
import page.Contact as contact
import page.Home as home
import page.SignUp as signup
import page.Login as login
import page.MyApp as myapp

with open("utils/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

optionsList = ['Home','Accounts','SignUp','Login','About','Contacts']

if 'user' in st.session_state:
    st.sidebar.success(f"Hi., {st.session_state['user']['email']}!")
    optionsList.remove("Home")
    optionsList.append("Logout")
    optionsList.insert(1,'MyApp')
    optionsList.remove("Login")
    optionsList.remove("Contacts")
    optionsList.remove("About")
    optionsList.remove("SignUp")
    print(st.session_state)
    
if 'user' not in st.session_state:
    optionsList.remove('Accounts')

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        with st.sidebar:        
            app = option_menu(
                menu_title='I-DOC TOOL ',
                options=optionsList,
                icons=['house-fill','person-circle','trophy-fill','chat-fill','info-circle-fill'],
                menu_icon='emoji-heart-eyes-fill',
                default_index=0,
                styles={
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "lightgray",},
        },
        )

        if app == 'Home':
            home.app()
        if app == 'MyApp':
            myapp.app()
        if app == 'Accounts':
            account.app()
        if app == 'About':
            about.app()
        if app == 'Contacts':
            contact.app()
        if app == 'SignUp':
            signup.app()
        if app == 'Login':
            login.app()
        if app == 'Logout':
            del st.session_state['user']
            st.success("You have been logged out.")
            st.rerun()
    
    
    run()
        