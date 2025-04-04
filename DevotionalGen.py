import streamlit as st
import pandas as pd
import ollama
import random

@st.cache_data
def load_bible():
    return pd.read_csv("D:/Shepherd OS/hf_datasets/bible.csv")

def app():
    df = load_bible()

    st.header("📜 AI-Powered Devotional Generator")
    st.write("Generate a personalized devotional based on any verse of your choice.")

    mode = st.radio("Verse Input Mode:", ["🔀 Random Verse", "✍️ Enter Manually"])

    if mode == "🔀 Random Verse":
        verse = df.sample(1).iloc[0]
        citation = verse['Citation']
        text = verse['Text']
    else:
        citation = st.text_input("Enter Citation (e.g., John 3:16)")
        text = st.text_area("Enter Verse Text")

    if st.button("✨ Generate Devotional") and citation and text:
        with st.spinner("Praying... I mean, Generating... 🙏"):
            prompt = f"""
You are a wise and compassionate Bible study companion. 
Reflect on the verse "{citation}: {text}"
Generate a devotional that includes:
- A brief reflection
- A personal application
- A heart-provoking question

Write in a warm, uplifting, and gentle tone.
"""
            try:
                response = ollama.chat(
                    model='mistral',
                    messages=[{"role": "user", "content": prompt}]
                )
                result = response['message']['content']
                st.markdown(f"### 📖 {citation}")
                st.write(f"**Verse:** {text}")
                st.markdown("#### 🙏 Devotional")
                st.markdown(result)
            except Exception as e:
                st.error("Is Ollama running? Failed to generate response.")
                st.exception(e)
