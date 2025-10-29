# app.py
import streamlit as st
import pandas as pd

# 1) config FIRST
st.set_page_config(
    page_title="Carbon Emissions Tracker",
    page_icon="🌱",
    layout="wide"
)

# 2) sidebar branding
st.logo(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Leaf_icon_02.svg/512px-Leaf_icon_02.svg.png",
    icon_image="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Leaf_icon_02.svg/64px-Leaf_icon_02.svg.png",
)
st.sidebar.markdown("### Analyst")
st.sidebar.page_link("app.py", label="🏠 Home")
st.sidebar.page_link("pages/01_Upload_Data.py", label="📤 Upload Data")
st.sidebar.page_link("pages/02_Recommendations.py", label="💡 Recommendations")
st.sidebar.page_link("pages/03_Dashboard.py", label="📊 Dashboard")
st.sidebar.page_link("pages/04_Emission_Factors.py", label="🧮 Emission Factors")
st.sidebar.page_link("pages/05_Reports.py", label="📑 Reports")

# 3) hero
st.markdown(
    """
    <div style="padding:28px 28px 20px;border-radius:18px;background:linear-gradient(90deg,#f0fdf4, #ecfeff);border:1px solid #e2e8f0;">
      <h1 style="margin:0;font-size:42px;">🌱 Analyst – Carbon Emissions Tracker</h1>
      <p style="margin:6px 0 0;font-size:18px;opacity:.9">
        Track <b>energy</b>, <b>transport</b>, and <b>waste</b>. Get dashboards and actionable reduction ideas.
      </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# optional banner image (helps the thumbnail)
st.image(
    "https://images.unsplash.com/photo-1469474968028-56623f02e42e?q=80&w=1600&auto=format&fit=crop",
    use_container_width=True,
)

# 4) quick nav (visible on first load -> better thumbnail)
c1, c2, c3 = st.columns(3)
with c1:
    st.page_link("pages/03_Dashboard.py", label="📊 Open Dashboard", use_container_width=True)
with c2:
    st.page_link("pages/01_Upload_Data.py", label="📤 Upload Data", use_container_width=True)
with c3:
    st.page_link("pages/02_Recommendations.py", label="💡 Recommendations", use_container_width=True)

st.divider()

# 5) KPI cards
k1, k2, k3, k4 = st.columns(4)
k1.metric("Monthly CO₂e", "12.4 t", "-8%")
k2.metric("Energy Intensity", "41.2 kWh/m²", "-5%")
k3.metric("Fleet CO₂e", "3.8 t", "-12%")
k4.metric("Recycling Rate", "63%", "+7 pts")

# 6) tiny chart (ensures a visual for the capture)
df = pd.DataFrame(
    {"Month": ["May","Jun","Jul","Aug","Sep","Oct"],
     "CO2e":  [15.1,14.6,14.2,13.5,12.9,12.4]}
)
st.line_chart(df, x="Month", y="CO2e", height=260)

# 7) keep your original CTA if you like (fixed the stray dot)
# if st.button("💡 Open Recommendations", use_container_width=True):
#     st.switch_page("pages/02_Recommendations.py")
