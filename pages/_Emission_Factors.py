import streamlit as st
from pathlib import Path
from src.core.factors import load_factors, save_factors
from src.core.models import EmissionFactors

st.title("🛠️ Emission Factors")
path = Path("factors.json")
ef = load_factors(path)

with st.form("ef"):
    st.write("Update numbers for your grid/region and year.")
    vals = ef.model_dump()
    for k in list(vals.keys()):
        if isinstance(vals[k], (int, float)) and "per_" in k:
            vals[k] = st.number_input(k, value=float(vals[k]), step=0.001, format="%.4f")
    region = st.text_input("region", value=ef.region or "")
    year = st.number_input("year", value=float(ef.year or 2025), step=1.0)
    submitted = st.form_submit_button("Save")
    if submitted:
        new = EmissionFactors(**{**vals, "region": region or None, "year": int(year)})
        save_factors(new, path)
        st.success("Saved emission factors.")
