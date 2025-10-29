import pandas as pd
from src.core.models import EmissionFactors
from src.calc.energy import compute_energy

def test_energy_basic():
    ef = EmissionFactors(electricity_kg_per_kwh=1.0, natural_gas_kg_per_kwh=1.0)
    df = pd.DataFrame({"electricity_kwh":[10], "natural_gas_kwh":[5]})
    out = compute_energy(df, ef)
    assert out["energy_co2e"].iloc[0] == 15
