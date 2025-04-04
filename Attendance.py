import streamlit as st
from datetime import datetime
import pandas as pd
from utils import load_data, save_data

def main():
    st.title("🕊️ Attendance Tracker")

    # Load members and attendance data
    members = load_data("members.csv")
    attendance = load_data("attendance.csv")

    today = datetime.today().strftime("%Y-%m-%d")
    
    # Option to log attendance
    st.subheader("Log Your Attendance")

    # Let the user choose their name
    name = st.selectbox("Select Your Name", members["Name"].tolist())

    if st.button("Mark Attendance"):
        # Mark attendance for today
        attendance = pd.concat([ 
            attendance, 
            pd.DataFrame([[name, today]], columns=["Name", "Date"])
        ], ignore_index=True)
        save_data(attendance, "attendance.csv")
        st.success("✅ Attendance marked for today")

    st.subheader("📅 Attendance Records")
    # Display attendance records
    st.dataframe(attendance)

if __name__ == "__main__":
    main()
