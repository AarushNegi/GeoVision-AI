from fastapi import APIRouter, UploadFile, File
from backend.app.vision.preprocess import preprocess

router = APIRouter()


@router.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    result = preprocess(file.file)

    return {
        "filename": file.filename,
        "original_size": result["original_size"],
        "processed_size": result["processed_size"]
    }