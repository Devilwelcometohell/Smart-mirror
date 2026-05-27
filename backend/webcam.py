import cv2
import time
import pyttsx3
import numpy as np

# 🔊 Voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

from clothing import detect_clothing
from hairstyle import detect_hairstyle
from posture import detect_posture
from logic import analyze


def run_webcam():
    # 🔹 Better camera driver (Windows)
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    # 🔹 High resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)

    if not cap.isOpened():
        print("Camera not found!")
        return

    print("Press Q to exit")

    last_spoken = ""
    last_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 🔥 Mirror effect
        frame = cv2.flip(frame, 1)

        # 🔹 Resize (performance balance)
        frame = cv2.resize(frame, (960, 720))

        # 🔹 Improve brightness & contrast
        frame = cv2.convertScaleAbs(frame, alpha=1.2, beta=20)

        # 🔹 Sharpen image
        kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
        frame = cv2.filter2D(frame, -1, kernel)

        # 🔥 AI detections
        cloth = detect_clothing(frame)
        hair = detect_hairstyle(frame)
        posture = detect_posture(frame)

        suggestions = analyze(cloth, hair, posture)

        # 🔊 VOICE LOGIC (FINAL)
        important = [s for s in suggestions if "Fix" in s or "Bad" in s or "straight" in s]

        speech_text = ". ".join(important)
        print("Speech:", speech_text)

        current_time = time.time()

        if speech_text:
            # Speak immediately if new
            if speech_text != last_spoken:
                speak(speech_text)
                last_spoken = speech_text
                last_time = current_time

            # Repeat after 5 seconds
            elif current_time - last_time > 5:
                speak(speech_text)
                last_time = current_time

        # -------- DISPLAY -------- #

        # 🔹 Clothing
        cv2.putText(frame, f"Cloth: {cloth['type']}", (10, 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

        # 🔹 Hairstyle
        cv2.putText(frame, f"Hair: {hair['suggestion']}", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

        # 🔹 Posture
        posture_color = (0, 255, 0) if "Good" in posture["posture"] else (0, 0, 255)

        cv2.putText(frame, f"Posture: {posture['posture']}", (10, 75),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, posture_color, 2)

        # 🔹 Suggestions
        y = 120
        for s in suggestions:
            cv2.putText(frame, s, (10, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.55, (0, 255, 0), 2)
            y += 25

        # 🔹 Grooming Score
        score = 100

        if posture["posture"] == "Bad posture":
            score -= 20

        if "messy" in hair["suggestion"].lower():
            score -= 20

        cv2.putText(frame, f"Grooming Score: {score}", (10, 440),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

        # Show window
        cv2.imshow("Smart Mirror", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # ✅ FPS control (IMPORTANT)
        time.sleep(0.5)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_webcam()