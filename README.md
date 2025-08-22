Simple Face Detector and Tracker



A lightweight Python application that detects and tracks human faces in real-time using your webcam. This project uses OpenCV's Haar Cascade classifier for efficient face detection.



Features


Real-time face detection using webcam

Basic face recognition by comparing detected faces to a reference image

Visual feedback with bounding boxes and labels

Simple size-based recognition (compares face area to reference)



Requirements


Python 3.x

OpenCV (pip install opencv-python)

NumPy (pip install numpy)



Limitations


Recognition is based only on face size, not advanced facial features

Lighting conditions and distance from camera affect accuracy

For better recognition, consider using more advanced methods like face embeddings
