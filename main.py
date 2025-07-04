from fastapi import FastAPI
from routers import aqi
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(aqi.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)