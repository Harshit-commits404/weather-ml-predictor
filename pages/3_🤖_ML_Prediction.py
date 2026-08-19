import streamlit as st
import pandas as pd
from utils.weather_api import get_coordinates, get_current_weather
from utils.model_utils import load_model, FEATURES

st.set_page_config(page_title="ML Prediction | WeatherAI", page_icon="🤖", layout="wide")
st.title("🤖 ML Temperature Prediction")

city = st.text_input("City for prediction", st.session_state.get("city","Prayagraj"))

if st.button("🚀 Fetch Live Data & Predict", use_container_width=True):
    try:
        coords = get_coordinates(city)
        weather = get_current_weather(coords["latitude"], coords["longitude"])
        model = load_model()
        row = pd.DataFrame([{
            "temperature": weather["temperature"],
            "humidity": weather["humidity"],
            "pressure": weather["pressure"],
            "wind_speed": weather["wind_speed"],
            "cloud_cover": weather["cloud_cover"],
        }])[FEATURES]
        pred = float(model.predict(row)[0])
        st.session_state["prediction"] = pred
        st.session_state["prediction_weather"] = weather
        st.session_state["prediction_city"] = coords["name"]
    except Exception as e:
        st.error(f"Prediction unavailable: {e}")

if "prediction" in st.session_state:
    w = st.session_state["prediction_weather"]
    c1,c2,c3 = st.columns(3)
    c1.metric("Current Temperature", f"{w['temperature']:.1f} °C")
    c2.metric("Predicted Temperature", f"{st.session_state['prediction']:.1f} °C")
    c3.metric("Difference", f"{st.session_state['prediction']-w['temperature']:+.1f} °C")
    st.caption("Note: the included demo model is trained on synthetic historical-like data.")
