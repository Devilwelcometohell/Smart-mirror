from ultralytics import YOLO

model = YOLO(r"C:\Users\Dell\Desktop\smart_mirror_backend\model\best.pt")

def detect_clothing(image):
    results = model.predict(image)
    
    probs = results[0].probs
    label = results[0].names[probs.top1]
    confidence = float(probs.top1conf)

    return {
        "type": label,
        "confidence": confidence
    }