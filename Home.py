import streamlit as st

st.set_page_config(page_title="Church Manager", layout="centered")
st.title("🙏 Welcome to ShepherdOS")
st.write("A simple, open-source platform for church management.")
st.markdown("---")

st.subheader("🧭 Navigation:")
st.markdown("- 📋 [Members](./pages/1_Members.py)")
st.markdown("- 🕊️ [Attendance](./pages/2_Attendance.py)")
st.markdown("- 💰 [Giving](./pages/3_Giving.py)")
st.markdown("- 📊 [Dashboard](./pages/4_Dashboard.py)")
