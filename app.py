# app.py (only if you use the button to navigate)
import streamlit as st
st.set_page_config(page_title="Carbon Emissions Tracker", page_icon="🌱", layout="wide")
st.title("🌱 Analyst – Carbon Emissions Tracker")
st.write("Track energy, transport, and waste. Get dashboards and reduction ideas.")

if st.button("💡 Open Recommendations", use_container_width=True):
    st.switch_page("pages/03_Recommendations.py")
