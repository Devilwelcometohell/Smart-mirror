import mediapipe as mp
import cv2

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

def detect_hairstyle(image):
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        h, w, _ = image.shape

        # Get landmarks
        landmarks = results.multi_face_landmarks[0].landmark

        # Forehead & top region (approx)
        forehead_y = landmarks[10].y * h   # top of forehead
        chin_y = landmarks[152].y * h

        face_height = chin_y - forehead_y

        # Heuristic: check if head is cut (hair not visible)
        if forehead_y < 20:
            return {
                "status": "Face detected",
                "hair_type": "not visible",
                "suggestion": "Adjust camera to include full hair"
            }

        # Heuristic: face tilt (bad grooming angle)
        left_eye = landmarks[33].y
        right_eye = landmarks[263].y

        if abs(left_eye - right_eye) > 0.02:
            return {
                "status": "Face detected",
                "hair_type": "unknown",
                "suggestion": "Keep your head straight"
            }

        # Default case
        return {
            "status": "Face detected",
            "hair_type": "normal",
            "suggestion": "Hair looks fine, maintain it properly"
        }

    else:
        return {
            "status": "No face",
            "hair_type": "unknown",
            "suggestion": "Adjust camera"
        }