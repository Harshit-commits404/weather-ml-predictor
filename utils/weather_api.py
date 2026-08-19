import requests

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

def get_coordinates(city: str):
    r = requests.get(GEOCODING_URL, params={"name": city, "count": 1, "language": "en", "format": "json"}, timeout=15)
    r.raise_for_status()
    data = r.json()
    if not data.get("results"):
        raise ValueError("City not found.")
    x = data["results"][0]
    return {"name": x["name"], "latitude": x["latitude"], "longitude": x["longitude"]}

def get_current_weather(latitude, longitude):
    params = {
        "latitude": latitude, "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,pressure_msl,wind_speed_10m,cloud_cover",
        "timezone": "auto"
    }
    r = requests.get(WEATHER_URL, params=params, timeout=15)
    r.raise_for_status()
    c = r.json()["current"]
    return {
        "temperature": c["temperature_2m"],
        "humidity": c["relative_humidity_2m"],
        "pressure": c["pressure_msl"],
        "wind_speed": c["wind_speed_10m"],
        "cloud_cover": c["cloud_cover"],
        "time": c["time"],
    }
