import pandas as pd
from pathlib import Path
from src.core.utils import read_any

def load_activities(path: Path) -> pd.DataFrame:
    df = read_any(path)
    df["date"] = pd.to_datetime(df["date"]).dt.date
    return df
