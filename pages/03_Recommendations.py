import streamlit as st
from src.calc.recs import recommend_actions

st.title("💡 Recommendations")

if "full_df" not in st.session_state:
    st.warning("Compute the dashboard first.")
    st.stop()

df = st.session_state["full_df"]
tips = recommend_actions(df)

st.subheader("Suggested actions")
for t in tips:
    st.write("• " + t)

st.info("These are heuristic suggestions. Refine with your local context and updated emission factors.")
