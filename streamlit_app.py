import streamlit as st
from crew_setup import run_crew
from analyzer import analyze_code

st.title("🧠 AI Multi-Agent Code Testing System")

code = st.text_area("Paste Python Code Here")

if st.button("Analyze Code"):
    st.json(analyze_code(code))

if st.button("Run AI Crew"):
    result = run_crew(code)
    st.write(result)
