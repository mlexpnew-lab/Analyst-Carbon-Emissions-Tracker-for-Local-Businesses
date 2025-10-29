
import streamlit as st
import pandas as pd
from pathlib import Path

st.title("📥 Upload Data")

upl = st.file_uploader("Upload CSV or Excel (.xlsx)", type=["csv", "xlsx"])
if upl:
    suffix = upl.name.split(".")[-1].lower()
    tmp = Path(f"uploaded.{suffix}")
    tmp.write_bytes(upl.getbuffer())

    if suffix == "csv":
        df = pd.read_csv(tmp)
    else:
        df = pd.read_excel(tmp)

    df["date"] = pd.to_datetime(df["date"]).dt.date
    st.session_state["activities_df"] = df
    st.success(f"Loaded {len(df)} rows.")
    st.dataframe(df.head(50))
