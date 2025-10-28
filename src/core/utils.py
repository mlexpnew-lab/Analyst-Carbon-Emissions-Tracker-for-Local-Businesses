import pandas as pd
from typing import Tuple

def read_any(path_or_buf) -> pd.DataFrame:
    p = str(path_or_buf).lower()
    if p.endswith(".csv"):
        return pd.read_csv(path_or_buf)
    if p.endswith(".xlsx") or p.endswith(".xls"):
        return pd.read_excel(path_or_buf)
    raise ValueError("Unsupported file type")

def split_features(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    meta = df[["date","business_unit"]]
    act = df.drop(columns=["date","business_unit"])
    return meta, act
