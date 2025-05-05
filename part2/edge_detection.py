import cv2
import numpy as np

def apply_edge_detection(frame):
    """Apply Canny edge detection to the frame"""
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply Canny edge detector
    edges = cv2.Canny(blurred, 100, 200)
    
    # Convert back to BGR for display
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
