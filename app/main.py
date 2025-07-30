from fastapi import FastAPI
from app.routes import model_routes

app = FastAPI(
    title="Deep Learning Model API",
    description="Upload and analyze PyTorch models",
    version="1.0.0"
)

# Include routes
app.include_router(model_routes.router, prefix="/model", tags=["Model Operations"])
