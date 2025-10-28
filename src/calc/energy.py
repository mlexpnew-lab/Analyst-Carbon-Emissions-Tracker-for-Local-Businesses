import pandas as pd
from src.core.models import EmissionFactors

def compute_energy(df: pd.DataFrame, ef: EmissionFactors) -> pd.DataFrame:
    out = pd.DataFrame(index=df.index)
    out["electricity_co2e"] = df["electricity_kwh"] * ef.electricity_kg_per_kwh
    out["natural_gas_co2e"] = df["natural_gas_kwh"] * ef.natural_gas_kg_per_kwh
    out["energy_co2e"] = out.sum(axis=1)
    return out
