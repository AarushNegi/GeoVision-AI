from fastapi import FastAPI
from backend.app.api.routes import router
app = FastAPI(
    title="GeoVision AI",
    version="0.1.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "GeoVision AI API"
    }