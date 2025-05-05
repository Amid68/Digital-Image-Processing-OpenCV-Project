import cv2
import numpy as np

def apply_soft_appearance(frame, diameter=9, sigma=75):
    """Apply bilateral filter for a soft, polished appearance"""
    # Bilateral filter preserves edges while smoothing
    return cv2.bilateralFilter(frame, diameter, sigma, sigma)
