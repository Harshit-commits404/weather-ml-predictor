from pathlib import Path
import json
import requests
import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

BASE = Path(__file__).resolve().parent
DATA = BASE / "data"
MODEL = BASE / "model"
DATA.mkdir(exist_ok=True)
MODEL.mkdir(exist_ok=True)

LAT, LON = 25.4358, 81.8463  # Prayagraj, India
START_DATE = "2024-01-01"
END_DATE = "2026-07-31"

URL = "https://archive-api.open-meteo.com/v1/archive"
HOURLY = "temperature_2m,relative_humidity_2m,surface_pressure,wind_speed_10m,cloud_cover"

print("Downloading real historical hourly weather data from Open-Meteo...")
params = {
    "latitude": LAT,
    "longitude": LON,
    "start_date": START_DATE,
    "end_date": END_DATE,
    "hourly": HOURLY,
    "timezone": "auto",
    "temperature_unit": "celsius",
    "wind_speed_unit": "kmh",
}
r = requests.get(URL, params=params, timeout=60)
r.raise_for_status()
payload = r.json()

if "hourly" not in payload:
    raise RuntimeError("Historical weather data was not returned by the API.")

h = payload["hourly"]
df = pd.DataFrame({
    "time": h["time"],
    "temperature": h["temperature_2m"],
    "humidity": h["relative_humidity_2m"],
    "pressure": h["surface_pressure"],
    "wind_speed": h["wind_speed_10m"],
    "cloud_cover": h["cloud_cover"],
})

df["time"] = pd.to_datetime(df["time"])
# Target is the actual temperature one hour later.
df["future_temperature"] = df["temperature"].shift(-1)
df = df.dropna().reset_index(drop=True)

features = ["temperature", "humidity", "pressure", "wind_speed", "cloud_cover"]
df = df.dropna(subset=features + ["future_temperature"])

# Save real historical dataset used for training.
df.to_csv(DATA / "weather_data.csv", index=False)

X = df[features]
y = df["future_temperature"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# Random Forest is still beginner-friendly and handles nonlinear weather relationships.
model = RandomForestRegressor(
    n_estimators=250,
    max_depth=14,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1,
)
model.fit(X_train, y_train)

pred = model.predict(X_test)
metrics = {
    "MAE": float(mean_absolute_error(y_test, pred)),
    "RMSE": float(np.sqrt(mean_squared_error(y_test, pred))),
    "R2": float(r2_score(y_test, pred)),
    "training_rows": int(len(df)),
    "location": "Prayagraj, India",
    "target": "temperature one hour ahead",
}

joblib.dump(model, MODEL / "weather_model.pkl")
with open(MODEL / "metrics.json", "w", encoding="utf-8") as f:
    json.dump(metrics, f, indent=2)

print("\nTraining complete!")
print(f"Real historical rows: {len(df):,}")
print(f"MAE : {metrics['MAE']:.3f} °C")
print(f"RMSE: {metrics['RMSE']:.3f} °C")
print(f"R²  : {metrics['R2']:.3f}")
print("\nModel saved to model/weather_model.pkl")
