import pandas as pd

def aggregate(meta: pd.DataFrame, energy: pd.DataFrame, transport: pd.DataFrame, waste: pd.DataFrame) -> pd.DataFrame:
    df = pd.concat([meta.reset_index(drop=True),
                    energy.reset_index(drop=True),
                    transport.reset_index(drop=True),
                    waste.reset_index(drop=True)], axis=1)
    df["total_co2e"] = df[["energy_co2e","transport_co2e","waste_co2e"]].sum(axis=1)
    return df
