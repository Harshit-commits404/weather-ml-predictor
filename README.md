# 🌦️ WeatherAI — Live Weather Temperature Prediction

A multi-page AI/ML weather analytics project using:

**Python • NumPy • Pandas • Matplotlib • Seaborn • Scikit-Learn • Streamlit**

## What makes this version real?
The training script downloads **real historical hourly weather data** from Open-Meteo for Prayagraj and creates a one-hour-ahead target using the actual next-hour temperature. Open-Meteo provides historical hourly temperature, humidity, pressure, wind speed and cloud-cover variables. citeturn0search0

The live prediction page then takes current API weather conditions and sends the same five features to the trained Random Forest model.

## Run

```bash
pip install -r requirements.txt
python train_model.py
streamlit run app.py
```

`python train_model.py` needs an internet connection because it downloads historical weather data.

## Pages
- Home
- Live Weather
- ML Prediction
- Analytics
- Model Information

## ML Features
- Temperature
- Relative humidity
- Surface pressure
- Wind speed
- Cloud cover

## Target
**Temperature one hour ahead**

## Data source
Open-Meteo Historical Weather API and Forecast API.

Historical API documentation: https://open-meteo.com/en/docs/historical-weather-api


## Deployment
See `DEPLOYMENT.md` for GitHub + Streamlit Community Cloud deployment steps.
