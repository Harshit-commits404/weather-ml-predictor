from pathlib import Path
import pandas as pd
import joblib
import json

BASE = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE / "model" / "weather_model.pkl"
DATA_PATH = BASE / "data" / "weather_data.csv"
METRICS_PATH = BASE / "model" / "metrics.json"

FEATURES = ["temperature","humidity","pressure","wind_speed","cloud_cover"]

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError("Model not found. Run train_model.py first.")
    return joblib.load(MODEL_PATH)

def load_dataset():
    return pd.read_csv(DATA_PATH)

def load_metrics():
    with open(METRICS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
