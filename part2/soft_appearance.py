import cv2
import numpy as np

def apply_soft_appearance(frame, diameter=9, sigma=75):
    return cv2.bilateralFilter(frame, diameter, sigma, sigma)
