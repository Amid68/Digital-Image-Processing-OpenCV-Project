import cv2
import numpy as np

def apply_contrast_enhancement(frame):
    yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    yuv[:,:,0] = cv2.equalizeHist(yuv[:,:,0])
    
    return cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
