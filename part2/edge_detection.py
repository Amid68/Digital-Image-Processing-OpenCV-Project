import cv2
import numpy as np

def apply_edge_detection(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 100, 200)
    
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
