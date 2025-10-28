import streamlit as st
from src.io.writers import to_csv, to_pdf_summary
from datetime import datetime

st.title("⬇️ Reports")

if "full_df" not in st.session_state:
    st.warning("Nothing to export yet.")
    st.stop()

df = st.session_state["full_df"]
tstamp = datetime.now().strftime("%Y%m%d_%H%M")
csv_path = f"report_{tstamp}.csv"
pdf_path = f"summary_{tstamp}.pdf"

if st.button("Export CSV"):
    to_csv(df, csv_path)
    st.success(f"Saved {csv_path}")
    with open(csv_path, "rb") as f:
        st.download_button("Download CSV", f, file_name=csv_path)

if st.button("Export PDF Summary"):
    to_pdf_summary(df, pdf_path)
    st.success(f"Saved {pdf_path}")
    with open(pdf_path, "rb") as f:
        st.download_button("Download PDF", f, file_name=pdf_path)
