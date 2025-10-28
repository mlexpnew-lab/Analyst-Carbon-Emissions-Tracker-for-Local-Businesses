import streamlit as st
from src.calc.recs import recommend_actions  # uses src/calc/recs.py

st.title("💡 Recommendations")

# Ensure the aggregated dataframe exists (computed on Dashboard)
if "full_df" not in st.session_state:
    st.warning("Please open 📊 Dashboard first to compute emissions.")
    st.stop()

df = st.session_state["full_df"]

# ✅ No joins, just pass the aggregated df
tips = recommend_actions(df)

st.subheader("Suggested actions")
if tips:
    for t in tips:
        st.write("• " + t)
else:
    st.info("No obvious actions yet. Add more months or data sources.")
