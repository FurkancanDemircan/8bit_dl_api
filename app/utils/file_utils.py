import os
from fastapi import UploadFile

UPLOAD_DIR = "models"

async def save_upload(file: UploadFile) -> str:
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    filepath = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(filepath, "wb") as f:
        contents = await file.read()
        f.write(contents)
    
    return filepath
