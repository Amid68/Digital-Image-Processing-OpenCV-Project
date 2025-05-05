import cv2
import numpy as np

def apply_cartoon_filter(frame):
    """Create a cartoon-like effect"""
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply median blur to reduce noise
    gray = cv2.medianBlur(gray, 5)
    
    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
        cv2.THRESH_BINARY, 9, 9
    )
    
    # Apply bilateral filter for color smoothing while preserving edges
    color = cv2.bilateralFilter(frame, 9, 300, 300)
    
    # Combine edges with color image
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    
    return cartoon
