import streamlit as st
import pandas as pd
from utils.weather_api import get_coordinates, get_current_weather

st.set_page_config(page_title="Live Weather | WeatherAI", page_icon="🌤️", layout="wide")
st.title("🌤️ Live Weather")

city = st.text_input("Enter city", "Prayagraj")
if st.button("🔄 Get Live Weather", use_container_width=True):
    with st.spinner("Fetching live weather..."):
        try:
            coords = get_coordinates(city)
            weather = get_current_weather(coords["latitude"], coords["longitude"])
            st.session_state["live_weather"] = weather
            st.session_state["city"] = coords["name"]
        except Exception as e:
            st.error(f"Could not fetch weather: {e}")

if "live_weather" in st.session_state:
    w = st.session_state["live_weather"]
    st.subheader(f"📍 {st.session_state['city']}")
    cols = st.columns(5)
    items = [
        ("🌡️ Temperature", f"{w['temperature']:.1f} °C"),
        ("💧 Humidity", f"{w['humidity']:.0f} %"),
        ("🧭 Pressure", f"{w['pressure']:.1f} hPa"),
        ("💨 Wind", f"{w['wind_speed']:.1f} km/h"),
        ("☁️ Cloud", f"{w['cloud_cover']:.0f} %"),
    ]
    for col,(label,val) in zip(cols,items):
        col.metric(label,val)
    st.caption(f"Weather time: {w['time']} | Source: Open-Meteo")
else:
    st.info("Enter a city and click **Get Live Weather**.")
