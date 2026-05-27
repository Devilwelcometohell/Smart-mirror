# Smart Mirror – AI Personal Assistant for Blind and Visually Impaired Users

Smart Mirror is an AI-powered assistive system designed to help blind and visually impaired users improve their grooming, posture, and overall appearance through real-time computer vision analysis and voice feedback.

The system analyzes a user’s image or live webcam feed to detect:

* 👕 Clothing type
* 💇 Hairstyle visibility and grooming
* 🧍 Body posture
* 💡 Personalized grooming suggestions

The project uses advanced AI and computer vision technologies such as **YOLOv8**, **MediaPipe**, **OpenCV**, **FastAPI**, and **React.js** to provide an accessible and interactive user experience.

## 🚀 Features

* Real-time clothing detection using YOLOv8
* Hairstyle and face analysis using MediaPipe
* Posture detection and correction suggestions
* Voice feedback for accessibility
* Modern React frontend UI
* FastAPI backend integration
* Image upload and webcam support
* Personalized grooming recommendations

## 🛠️ Technologies Used

### Frontend

* React.js
* Tailwind CSS
* Vite

### Backend

* FastAPI
* Python

### AI / Computer Vision

* YOLOv8
* MediaPipe
* OpenCV
* NumPy
* pyttsx3 (Text-to-Speech)

## 📌 How It Works

1. User uploads an image or uses webcam input
2. Backend processes the image using AI models
3. YOLOv8 detects clothing
4. MediaPipe analyzes face and posture
5. Logic module generates grooming suggestions
6. Frontend displays results with accessibility-focused UI
7. Voice engine provides spoken feedback

## 🎯 Project Goal

The main goal of this project is to provide independence and confidence to visually impaired users by helping them understand their appearance through AI-powered assistance.

## 📂 Project Modules

* `frontend/` → React frontend
* `backend/` → FastAPI backend
* `clothing.py` → Clothing detection using YOLOv8
* `hairstyle.py` → Hairstyle analysis
* `posture.py` → Posture detection
* `logic.py` → Suggestion generation
* `main.py` → API endpoints

## ▶️ Run the Project

### Backend

```bash
cd backend
python -m uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## 📖 Future Improvements

* Emotion detection
* Real-time voice conversation
* Mobile application support
* Smart mirror hardware integration
* Personalized fashion recommendations


## 👨‍💻 Developed By

Devang Shukla
B.Tech Electronics & Communication Engineering (VLSI)
GLA University
