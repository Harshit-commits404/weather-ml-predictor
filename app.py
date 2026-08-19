import streamlit as st

st.set_page_config(
    page_title="WeatherAI | ML Predictor",
    page_icon="🌦️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
.stApp {background: linear-gradient(135deg,#07111f 0%,#0b1729 50%,#101c31 100%); color:#eef6ff;}
.block-container {padding-top:2rem; max-width:1250px;}
.hero {padding:42px 10px 28px;}
.hero h1 {font-size:48px; margin-bottom:8px;}
.hero p {font-size:18px; color:#a9bfd7;}
.card {background:rgba(255,255,255,.06); border:1px solid rgba(255,255,255,.1); border-radius:20px; padding:24px; margin:8px 0;}
.badge {display:inline-block; padding:7px 12px; border-radius:20px; background:rgba(76,201,240,.14); color:#76d9ff; font-size:13px;}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🌦️ WeatherAI")
st.sidebar.caption("Live Weather + Machine Learning")

st.markdown("""
<div class="hero">
<span class="badge">AI / ML WEATHER ANALYTICS</span>
<h1>Live Weather Temperature Predictor</h1>
<p>Use live weather conditions and a trained machine-learning model to estimate near-future temperature.</p>
</div>
""", unsafe_allow_html=True)

c1,c2,c3 = st.columns(3)
with c1:
    st.markdown('<div class="card"><h3>🌤️ Live Data</h3><p>Fetch current weather conditions for any supported city.</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card"><h3>🤖 ML Prediction</h3><p>Predict temperature from humidity, pressure, wind and other features.</p></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="card"><h3>📊 Analytics</h3><p>Explore correlations, trends and model performance.</p></div>', unsafe_allow_html=True)

st.info("Use the pages in the sidebar to explore live weather, prediction, analytics and model information.")
