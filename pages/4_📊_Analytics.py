import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils.model_utils import load_dataset

st.set_page_config(page_title="Analytics | WeatherAI", page_icon="📊", layout="wide")
st.title("📊 Weather Analytics")
st.caption("Analytics are generated from the real historical hourly weather dataset used for model training.")

df = load_dataset()
st.write(f"Dataset rows: **{len(df):,}**")

fig1, ax1 = plt.subplots(figsize=(10,4))
ax1.plot(df.index, df["temperature"])
ax1.set_title("Temperature Trend")
ax1.set_xlabel("Sample")
ax1.set_ylabel("Temperature (°C)")
st.pyplot(fig1)

st.subheader("Feature Correlation")
fig2, ax2 = plt.subplots(figsize=(8,5))
sns.heatmap(df[["temperature","humidity","pressure","wind_speed","cloud_cover"]].corr(), annot=True, fmt=".2f", ax=ax2)
st.pyplot(fig2)

st.subheader("Preview")
st.dataframe(df.head(20), use_container_width=True)
