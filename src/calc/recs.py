# src/calc/recs.py
import pandas as pd

def recommend_actions(df: pd.DataFrame) -> list[str]:
    tips: set[str] = set()
    # simple heuristics based on aggregated columns produced on the Dashboard
    if "electricity_co2e" in df and "total_co2e" in df:
        if df["electricity_co2e"].mean() > df["total_co2e"].mean() * 0.4:
            tips.add("Audit HVAC schedules and upgrade to LED/efficient equipment to cut grid kWh by 10–20%.")
    if "flight_co2e" in df and df["flight_co2e"].sum() > 0:
        tips.add("Replace short-haul flights (<800 km) with rail or virtual meetings.")
    if "landfill_co2e" in df and "waste_co2e" in df:
        if df["landfill_co2e"].mean() > df["waste_co2e"].mean() * 0.5:
            tips.add("Introduce waste segregation training and add compost/recycling pickup.")
    if "fleet_km_co2e" in df and df["fleet_km_co2e"].sum() > 0:
        tips.add("Batch deliveries and optimize routes; track km per delivery KPI.")
    return sorted(tips)
