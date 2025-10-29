import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def monthly_trend_forecast(df: pd.DataFrame, value_col: str = "total_co2e", steps: int = 6) -> pd.DataFrame:
    tmp = df.groupby("date", as_index=False)[value_col].sum().sort_values("date")
    tmp["t"] = np.arange(len(tmp))
    model = LinearRegression().fit(tmp[["t"]], tmp[value_col])
    future_t = np.arange(len(tmp), len(tmp)+steps)
    future = pd.DataFrame({"t": future_t})
    future[value_col] = model.predict(future[["t"]])
    future["date"] = pd.date_range(tmp["date"].max(), periods=steps+1, freq="MS")[1:]
    return future[["date", value_col]]
