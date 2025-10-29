import pandas as pd
from src.core.models import EmissionFactors

def compute_waste(df: pd.DataFrame, ef: EmissionFactors) -> pd.DataFrame:
    out = pd.DataFrame(index=df.index)
    out["landfill_co2e"] = df["landfill_kg"] * ef.landfill_kg_per_kg
    out["recycle_co2e"] = df["recycle_kg"] * ef.recycle_kg_per_kg
    out["compost_co2e"] = df["compost_kg"] * ef.compost_kg_per_kg
    out["waste_co2e"] = out.sum(axis=1)
    return out
