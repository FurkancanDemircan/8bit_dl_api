from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services import model_service

router = APIRouter()

@router.post("/upload/")
async def upload_model(file: UploadFile = File(...)):
    """Upload a PyTorch .pth model and get its layers."""
    if not file.filename.endswith(".pth"):
        raise HTTPException(status_code=400, detail="File must be a .pth model file")
    
    layers = await model_service.load_and_inspect(file)
    return {"filename": file.filename, "layers": layers}

@router.post("/extract-features/")
async def extract_features(file: UploadFile = File(...)):
    """Extract features from an uploaded .pth model."""
    features = await model_service.extract_features(file)
    return {"filename": file.filename, "features": features}
