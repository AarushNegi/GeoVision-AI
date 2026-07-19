from fastapi import APIRouter, UploadFile, File
from PIL import Image

router = APIRouter()


@router.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    image = Image.open(file.file)

    return {
        "filename": file.filename,
        "width": image.width,
        "height": image.height,
        "format": image.format
    }