import cv2
import numpy as np

# Load Haar Cascade (already installed with OpenCV)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Load your saved face (enroll first)
try:
    reference_img = cv2.imread("my_face.jpg", 0)  # Grayscale
    if reference_img is None:
        raise FileNotFoundError
except:
    print("Error: Save a reference photo as 'my_face.jpg' first.")
    exit()

# Initialize camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    
    for (x, y, w, h) in faces:
        # Simple check: Compare face size to reference (adjust threshold)
        face_ratio = (w * h) / (reference_img.shape[0] * reference_img.shape[1])
        is_you = 0.7 < face_ratio < 1.3  # True if face size is close to reference
        
        color = (0, 255, 0) if is_you else (0, 0, 255)
        label = "YOU" if is_you else "Unknown"
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, label, (x, y-10), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
    
    cv2.imshow("Press 'q' to quit", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()