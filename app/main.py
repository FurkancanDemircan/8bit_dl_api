from fastapi import FastAPI
from app.routes import model_routes

app = FastAPI(
    title="Deep Learning Model API",
    description="Upload and analyze PyTorch models",
    version="1.0.0"
)

# Include routes
app.include_router(model_routes.router, prefix="/model", tags=["Model Operations"])

origins = [
    "http://localhost:3000",  # React dev server
    "https://zp1v56uxy8rdx5ypatb0ockcb9tr6a-oci3--5173--96435430.local-credentialless.webcontainer-api.io", # Your preview link
    "https://your-frontend-domain.com",  # Replace with your production frontend domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # allow these domains
    allow_credentials=True,
    allow_methods=["*"],          # allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],          # allow all headers (Authorization, Content-Type, etc.)
)
