from ingest_data import ingest_weather_data
import pandas as pd

def transform_weather_data(daily: dict) -> pd.DataFrame:
    df = pd.DataFrame(daily)
    df["time"] = pd.to_datetime(df["time"])
    return df
