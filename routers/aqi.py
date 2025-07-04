from fastapi import APIRouter, Query
from services.fetch_aqi import get_ground_aqi, get_satellite_aqi
from services.forecast_model import forecast_aqi
from services.health import health_recommendation

router = APIRouter()

@router.get("/aqi")
def get_aqi(lat: float, lon: float):
    ground = get_ground_aqi(lat, lon)
    satellite = get_satellite_aqi(lat, lon)
    current = ground['data']['current']['pollution']['aqius']
    forecast = forecast_aqi(current, 72)
    health_msg = health_recommendation(current)

    return {
        "location": ground["data"]["city"],
        "ground_aqi": current,
        "satellite_data": satellite,
        "forecast": forecast,
        "health": health_msg
    }