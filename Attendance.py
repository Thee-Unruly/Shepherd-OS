import streamlit as st
from datetime import datetime
import pandas as pd
from utils import load_data, save_data

st.title("🕊️ Attendance Tracker")

members = load_data("members.csv")
attendance = load_data("attendance.csv")

today = datetime.today().strftime("%Y-%m-%d")
selected = st.multiselect("Select attendees for today", members["Name"].tolist())

if st.button("Save Attendance"):
    for name in selected:
        attendance = pd.concat([
            attendance,
            pd.DataFrame([[name, today]], columns=["Name", "Date"])
        ], ignore_index=True)
    save_data(attendance, "attendance.csv")
    st.success("✅ Attendance saved")

st.subheader("📅 Attendance Records")
st.dataframe(attendance)
