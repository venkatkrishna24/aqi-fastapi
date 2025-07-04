import requests

def get_ground_aqi(lat, lon):
    api_key = "YOUR_IQAIR_API_KEY"
    url = f"http://api.airvisual.com/v2/nearest_city?lat={lat}&lon={lon}&key={api_key}"
    response = requests.get(url)
    return response.json()

def get_satellite_aqi(lat, lon):
    # Placeholder: Replace with real NASA API or Sentinel-5P source
    return {
        "pm25": 80,
        "no2": 25,
        "o3": 40,
        "source": "satellite"
    }