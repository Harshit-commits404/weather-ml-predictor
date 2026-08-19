import streamlit as st
from utils.model_utils import load_metrics

st.set_page_config(page_title="Model Info | WeatherAI", page_icon="🧠", layout="wide")
st.title("🧠 Model Information")

metrics = load_metrics()
st.markdown("""
### Algorithm
**Random Forest Regressor**

### Input Features
- Current temperature
- Humidity
- Atmospheric pressure
- Wind speed
- Cloud cover

### Target
Actual temperature one hour ahead.

### Libraries
Python • NumPy • Pandas • Scikit-Learn • Matplotlib • Seaborn • Streamlit
""")

c1,c2,c3 = st.columns(3)
c1.metric("MAE", f"{metrics['MAE']:.3f} °C")
c2.metric("RMSE", f"{metrics['RMSE']:.3f} °C")
c3.metric("R² Score", f"{metrics['R2']:.3f}")

st.warning("The included model is a ready-to-run demo model. For the final academic version, run `python train_model.py` locally to replace it with a model trained on real historical hourly Open-Meteo observations.")
