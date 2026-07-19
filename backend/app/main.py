from fastapi import FastAPI

app = FastAPI(
    title="GeoVision AI",
    version="0.1.0",
    description="AI-powered image geolocation platform"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to GeoVision AI 🚀"
    }