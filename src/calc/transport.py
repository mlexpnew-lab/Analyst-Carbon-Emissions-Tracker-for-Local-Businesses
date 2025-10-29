import pandas as pd
from src.core.models import EmissionFactors

def compute_transport(df: pd.DataFrame, ef: EmissionFactors) -> pd.DataFrame:
    out = pd.DataFrame(index=df.index)
    out["diesel_co2e"] = df["diesel_l"] * ef.diesel_kg_per_l
    out["petrol_co2e"] = df["petrol_l"] * ef.petrol_kg_per_l
    out["fleet_km_co2e"] = df["vehicle_km_wfo"] * ef.vehicle_kg_per_km
    out["flight_co2e"] = df["flight_km"] * ef.flight_kg_per_km
    out["transport_co2e"] = out.sum(axis=1)
    return out
