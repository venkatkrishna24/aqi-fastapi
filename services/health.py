def health_recommendation(aqi):
    if aqi < 50:
        return "Good – No precautions needed."
    elif aqi < 100:
        return "Moderate – Sensitive individuals should reduce outdoor activity."
    elif aqi < 200:
        return "Unhealthy – Wear masks outdoors."
    else:
        return "Very Unhealthy – Avoid going outside."