def forecast_aqi(current_aqi, hours=24):
    return [current_aqi + i*2 for i in range(hours // 3)]