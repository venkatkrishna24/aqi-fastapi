from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from aqi import router as aqi_router

app = FastAPI()

# CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AQI backend is live with modular routes"}

# Mount AQI route
app.include_router(aqi_router)
