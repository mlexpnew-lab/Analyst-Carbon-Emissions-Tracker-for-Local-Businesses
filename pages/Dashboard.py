import streamlit as st, pandas as pd, plotly.express as px
from pathlib import Path
from src.core.factors import load_factors
from src.core.utils import split_features
from src.calc.energy import compute_energy
from src.calc.transport import compute_transport
from src.calc.waste import compute_waste
from src.calc.aggregate import aggregate
from src.calc.forecast import monthly_trend_forecast

st.title("📊 Dashboard")

if "activities_df" not in st.session_state:
    st.warning("Go to Upload page first.")
    st.stop()

acts = st.session_state["activities_df"].copy()
ef_path = Path("factors.json")
ef = load_factors(ef_path)

meta, act = split_features(acts)
en = compute_energy(act, ef)
tr = compute_transport(act, ef)
wa = compute_waste(act, ef)
full = aggregate(meta, en, tr, wa)

st.metric("Total CO₂e (kg)", f"{full['total_co2e'].sum():,.0f}")
st.metric("Avg per month (kg)", f"{full.groupby('date')['total_co2e'].sum().mean():,.0f}")

by_month = full.groupby("date", as_index=False)["total_co2e"].sum()
fig = px.line(by_month, x="date", y="total_co2e", title="Total CO₂e by Month")
st.plotly_chart(fig, use_container_width=True)

by_bu = full.groupby("business_unit", as_index=False)["total_co2e"].sum().sort_values("total_co2e", ascending=False)
fig2 = px.bar(by_bu, x="business_unit", y="total_co2e", title="By Business Unit")
st.plotly_chart(fig2, use_container_width=True)

if st.checkbox("Show 6-month forecast (simple linear trend)"):
    fc = monthly_trend_forecast(full)
    fig3 = px.line(fc, x="date", y="total_co2e", title="Forecast CO₂e (Next 6 months)")
    st.plotly_chart(fig3, use_container_width=True)

st.session_state["full_df"] = full
