# person_detect.py - GitHub ready
import cv2
import numpy as np

def detect_person(image_path):
    # Load image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # HOG + SVM people detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    
    # Detect (scale for accuracy)
    boxes, weights = hog.detectMultiScale(gray, winStride=(4,4), padding=(8,8), scale=1.05)
    
    person_present = len(boxes) > 0
    print(f"Person present: {person_present} (Detections: {len(boxes)})")
    
    # Draw boxes
    for (x,y,w,h) in boxes:
        cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)
    
    cv2.imshow('Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return person_present

# Test
detect_person('your_image.jpg')  # Replace with test img
