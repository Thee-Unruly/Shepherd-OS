import streamlit as st
import pandas as pd
from utils import load_data, save_data

st.title("📋 Members")
members = load_data("members.csv")

with st.form("add_member"):
    name = st.text_input("Full Name")
    phone = st.text_input("Phone")
    group = st.selectbox("Ministry Group", ["Youth", "Worship", "Ushering", "None"])
    submitted = st.form_submit_button("Add Member")
    if submitted and name:
        new_member = pd.DataFrame([[name, phone, group]], columns=["Name", "Phone", "Group"])
        members = pd.concat([members, new_member], ignore_index=True)
        save_data(members, "members.csv")
        st.success("✅ Member added!")

st.subheader("👥 Members List")
st.dataframe(members)
