import streamlit as st
import importlib

st.set_page_config(page_title="📖 BibleStudyAI", layout="wide")
st.title("✝️ Bible Study AI Platform")

pages = {
    "Devotional Generator": "DevotionalGen",
    "Discipleship Coach": "DiscipleshipCoach"
}

page = st.sidebar.radio("📘 Navigate", list(pages.keys()))
module = importlib.import_module(pages[page])
module.app()
