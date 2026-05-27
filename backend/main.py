from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import cv2
import numpy as np

from clothing import detect_clothing
from hairstyle import detect_hairstyle
from posture import detect_posture
from logic import analyze

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    contents = await file.read()
    np_arr = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    cloth = detect_clothing(image)
    hair = detect_hairstyle(image)
    posture = detect_posture(image)

    suggestions = analyze(cloth, hair, posture)

    return {
        "clothing": cloth,
        "hairstyle": hair,
        "posture": posture,
        "suggestions": suggestions
    }

# cd C:\Users\Dell\Desktop\smart_mirror_backend\backend
# python -m uvicorn main:app --reload
# http://127.0.0.1:8000/docs
# cd C:\Users\Dell\Desktop\smart_mirror_backend\frontend
# npm run dev
# http://localhost:5173/http://localhost:5173/
# python webcam