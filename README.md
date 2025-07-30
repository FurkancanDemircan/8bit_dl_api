# 8bit Deep Learning Model API
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-brightgreen?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A FastAPI-based REST API for uploading and analyzing PyTorch `.pth` models.  
It supports model inspection and feature extraction.
## 🚀 Features
- Upload and inspect PyTorch `.pth` models
- Extract features such as total parameters
- Interactive Swagger UI included
- Ready for cloud deployment

---

### 🔧 Installation & Run
<details>
  <summary>Installation Commands</summary>

```bash
# Clone project
git clone https://github.com/your-username/8bit_dl_api.git
cd 8bit_dl_api

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Run the server
python run.py
"""
The server will be available at:
	•	API Root: http://127.0.0.1:8000
	•	Swagger UI: http://127.0.0.1:8000/docs
"""
```
</details>

---

## 📂 Project Structure

```bash
fastapi_model_api/
│
├── app/
│   ├── main.py
│   ├── routes/
│   │   └── model_routes.py
│   ├── services/
│   │   └── model_service.py
│   └── utils/
│       └── file_utils.py
│
├── models/                 # Uploaded .pth files
├── requirements.txt
└── run.py
```

---

## 📌 Endpoints
<ul>
<li>Upload Model</li>
  POST /model/upload/
  
```bash
curl -X POST "http://127.0.0.1:8000/model/upload/" \
  -F "file=@resnet50.pth"
```


<details>
  <summary>Response Example</summary>
  
```bash
{
  "filename": "resnet50.pth",
  "layers": [
    "Conv2d(3, 64, kernel_size=(7,7), stride=(2,2), padding=(3,3), bias=False)",
    "BatchNorm2d(64, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)",
    "ReLU(inplace=True)"
  ]
}
```
</details>

<li>Extract Features</li>

POST /model/extract-features/

```bash
curl -X POST "http://127.0.0.1:8000/model/extract-features/" \
  -F "file=@resnet50.pth"
```

<details>
  <summary>Response Example</summary>

```bash
{
  "filename": "resnet50.pth",
  "features": {
    "total_parameters": 23534532
  }
}
```
</details>

</ul>

---

## 🛠️ Dependencies

Add to requirements.txt:
```bash
fastapi
uvicorn
torch
pydantic
```
Install with:
```bash
pip install -r requirements.txt
```

---

### 🌐 Deployment

Local Run
```bash
python run.py
```

Cloud Deployment (Render / Railway)
	•	Push repo to GitHub
	•	Connect service and set start command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

## 📄 License

MIT License. Free to use and modify.

---

⚡ If you like, I can also add a **section at the bottom of this README with an HTML + JS client snippet** that shows how your webpage can upload a `.pth` file directly to this API.  
Do you want me to add that?
