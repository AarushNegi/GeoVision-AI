from fastapi import APIRouter, UploadFile, File
from backend.app.vision.preprocess import preprocess
from backend.app.vision.feature_extractor import extract_features
from backend.app.vision.preprocess import preprocess
from backend.app.vision.feature_extractor import extract_features

router = APIRouter()


@router.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):

    result = preprocess(file.file)

    embedding = extract_features(result["tensor"])

    return {
        "filename": file.filename,
        "original_size": list(result["original_size"]),
        "processed_size": list(result["processed_size"]),
        "embedding_dimension": embedding.shape[0]
    }