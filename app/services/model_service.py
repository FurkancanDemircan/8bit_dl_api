import torch
from app.utils import file_utils
from fastapi import UploadFile

async def load_and_inspect(file: UploadFile):
    path = await file_utils.save_upload(file)

    # Load PyTorch model
    model = torch.load(path, map_location="cpu")
    model.eval()

    # Get readable list of layers
    layers = [str(layer) for layer in model.children()]
    return layers

async def extract_features(file: UploadFile):
    path = await file_utils.save_upload(file)

    model = torch.load(path, map_location="cpu")
    model.eval()

    # Dummy example: return parameter count
    total_params = sum(p.numel() for p in model.parameters())
    return {"total_parameters": total_params}
