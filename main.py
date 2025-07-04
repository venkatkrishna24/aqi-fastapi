from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from aqi import router as aqi_router

app = FastAPI()

# Allow access from frontend (Flutter, web, etc.)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AQI FastAPI backend is working!"}

@app.get("/aqi")
def get_aqi(lat: float = Query(...), lon: float = Query(...)):
    # Moderate air quality data example (based on lat/lon)
    return {
        "location": f"Location at lat={lat}, lon={lon}",
        "ground_aqi": 92,  # Moderate level
        "satellite_aqi": 90,
        "forecast": [85, 89, 94],  # next 24–72 hours
        "health": "Moderate air quality. Unusually sensitive individuals should consider limiting prolonged outdoor exertion."
    }
