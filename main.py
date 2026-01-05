# FastAPI server and endpoints

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import AnalyzeRequest, AnalyzeResponse
from scam_detector import detect_scam

app = FastAPI(title="Linzi AI Scam Detector")

# Enable CORS for frontend (React or any web app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For demo; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Linzi AI Scam Detector Backend is running!"}

@app.post("/api/v1/analyze", response_model=AnalyzeResponse)
def analyze_message(request: AnalyzeRequest):
    if not request.consent:
        raise HTTPException(status_code=400, detail="User consent required")
    if not request.text:
        raise HTTPException(status_code=400, detail="No text provided for analysis")

    result = detect_scam(request.text)
    return result
