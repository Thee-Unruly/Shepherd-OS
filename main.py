import streamlit as st
from streamlit_option_menu import option_menu
import Home
import Attendance
import Dashboard
import DevotionalGen
import DiscipleshipCoach
import Members
import login  # Import the login module
import chat

# Set page configuration once at the top of the main script
st.set_page_config(
    page_title="SHEPHERD OS",
    layout="wide"
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        # Show login page if not logged in
        if "logged_in" not in st.session_state or not st.session_state.logged_in:
            login.main()
            return

        # Show logout button in sidebar
        with st.sidebar:
            if st.button("Logout"):
                st.session_state.logged_in = False
                st.rerun()  # Reload to show login page

            selected_page = option_menu(
                menu_title="SHEPHERD OS",
                options=['Dashboard', 'Attendance', 'Discipleship Coach', 'Devotional Generator', 'Members', 'Chat'],
                icons=['house-fill', 'person-check-fill', 'people-fill', 'lightbulb-fill', 'person-lines-fill', 'chat-dots'],
                menu_icon='menu-button-wide',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": "#333"},
                    "icon": {"color": "white", "font-size": "13px"}, 
                    "nav-link": {"color": "white", "font-size": "13px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        # Display the selected page's content
        if selected_page == 'Dashboard':
            Dashboard.main()
        elif selected_page == 'Attendance':
            Attendance.main()
        elif selected_page == 'Discipleship Coach':
            DiscipleshipCoach.main()
        elif selected_page == 'Devotional Generator':
            DevotionalGen.main()
        elif selected_page == 'Members':
            Members.main()
        elif selected_page == 'Chat':
            chat.main()

if __name__ == "__main__":
    multi_app = MultiApp()
    multi_app.run()
