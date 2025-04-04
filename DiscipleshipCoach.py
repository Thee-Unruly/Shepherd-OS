import streamlit as st
import pandas as pd
from datetime import datetime

@st.cache_data
def get_default_data():
    return pd.DataFrame(columns=["Date", "Verse", "Topic", "Reflection", "Completed"])

def app():
    st.header("📅 Discipleship Coach")
    st.write("Track your spiritual growth and devotional habits.")

    if "tracker" not in st.session_state:
        st.session_state.tracker = get_default_data()

    with st.form("track_devotion"):
        date = st.date_input("Date", value=datetime.today())
        verse = st.text_input("Bible Verse")
        topic = st.text_input("Topic or Focus")
        reflection = st.text_area("Reflection / Insight")
        completed = st.checkbox("✅ Mark as Completed")

        submitted = st.form_submit_button("💾 Save Entry")
        if submitted:
            new_entry = {
                "Date": date,
                "Verse": verse,
                "Topic": topic,
                "Reflection": reflection,
                "Completed": completed
            }
            st.session_state.tracker = pd.concat(
                [st.session_state.tracker, pd.DataFrame([new_entry])],
                ignore_index=True
            )
            st.success("Devotional entry saved.")

    st.markdown("---")
    st.subheader("📘 Your Discipleship Journal")
    st.dataframe(st.session_state.tracker, use_container_width=True)
