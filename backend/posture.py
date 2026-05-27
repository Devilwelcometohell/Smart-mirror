import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

def detect_posture(image):
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb)

    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark
        
        shoulder_y = landmarks[11].y
        hip_y = landmarks[23].y

        if abs(shoulder_y - hip_y) < 0.1:
            posture_status = "Good posture"
        else:
            posture_status = "Bad posture"

        return {
            "posture": posture_status,
            "suggestion": "Keep your back straight"
        }
    else:
        return {
            "posture": "Not detected",
            "suggestion": "Stand properly"
        }