import streamlit as st
import importlib

st.set_page_config(page_title="📖 BibleStudyAI", layout="wide")
st.title("✝️ Bible Study AI Platform")

pages = {
    "Devotional Generator": "DevotionalGen",
    "Discipleship Coach": "DiscipleshipCoach"
}

page = st.sidebar.radio("📘 Navigate", list(pages.keys()))
module_name = pages[page]

try:
    # Dynamically import the selected module
    module = importlib.import_module(module_name)
    
    # Check if the module has the 'main()' function
    if hasattr(module, 'main'):
        module.main()  # Call the 'main' function
    else:
        st.error(f"Error: The module '{module_name}' does not have a 'main()' function.")
except ModuleNotFoundError:
    st.error(f"Error: The module '{module_name}' could not be found.")
