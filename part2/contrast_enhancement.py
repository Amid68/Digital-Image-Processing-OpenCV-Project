import cv2
import numpy as np

def apply_contrast_enhancement(frame):
    """Enhance contrast using histogram equalization"""
    # Convert to YUV color space (Y: luminance, U/V: chrominance)
    yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    
    # Apply histogram equalization to the Y channel
    yuv[:,:,0] = cv2.equalizeHist(yuv[:,:,0])
    
    # Convert back to BGR
    return cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
