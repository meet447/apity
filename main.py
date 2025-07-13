from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.weather import router as weather_router
from routes.ip import router as ip_router
from routes.search import router as search_router

app = FastAPI(title="Apity")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(weather_router, prefix="")
app.include_router(ip_router, prefix="")
app.include_router(search_router, prefix="")

app.get("/")
def root():
    return {"message": "all services working"}
