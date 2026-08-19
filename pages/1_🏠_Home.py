import streamlit as st
st.set_page_config(page_title="Home | WeatherAI", page_icon="🏠", layout="wide")
st.title("🏠 Home")
st.write("Welcome to WeatherAI — a beginner-friendly machine learning weather analytics system.")
st.markdown("""
### Project workflow
1. Live weather data is collected from a weather API.
2. Pandas and NumPy prepare the data.
3. Scikit-Learn uses historical weather data to train a regression model.
4. The current live conditions are passed to the trained model.
5. Matplotlib and Seaborn visualize weather patterns and model results.
""")
st.success("Start with **Live Weather** from the sidebar.")
