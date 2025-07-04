from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend access (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "AQI FastAPI is live"}

@app.get("/aqi")
def get_aqi(city: str = None, lat: float = None, lon: float = None):
    if city:
        return {
            "source": "city",
            "city": city,
            "aqi": 92,
            "category": "Moderate",
            "forecast": [89, 90, 93, 91, 94, 92, 90]
        }
    elif lat is not None and lon is not None:
        return {
            "source": "coordinates",
            "lat": lat,
            "lon": lon,
            "aqi": 85,
            "category": "Moderate",
            "forecast": [83, 84, 86, 85, 87, 86, 85]
        }
    else:
        return {"error": "Please provide either a city or coordinates (lat/lon)"}

