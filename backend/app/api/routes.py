from fastapi import APIRouter, UploadFile, File
from backend.app.vision.preprocess import preprocess
from backend.app.vision.feature_extractor import extract_features

router = APIRouter()


@router.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    result = preprocess(file.file)

    features = extract_features(result["tensor"])

    return {
        "filename": file.filename,
        "embedding_dimension": features.shape[0],
        "processed_size": list(result["processed_size"])
    }