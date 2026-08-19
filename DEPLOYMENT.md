# Free Deployment — Streamlit Community Cloud

## 1. Test locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 2. GitHub
Create a new **public** GitHub repository and upload the contents of this folder.

Do not upload API keys or passwords. This project uses Open-Meteo and does not require a secret API key.

## 3. Streamlit Community Cloud
Create a new app and select:
- Repository: your GitHub repository
- Branch: `main`
- Main file: `app.py`

Then deploy.

## 4. Important
The included `model/weather_model.pkl` lets the app start immediately. The `train_model.py` script can download real historical hourly weather data and retrain the model when run locally.

For a final academic submission, run:
```bash
python train_model.py
```
then commit the newly generated `data/weather_data.csv` and `model/weather_model.pkl` to GitHub before deployment.

The deployed app uses the saved model and live Open-Meteo weather conditions; it does not retrain on every page load.
