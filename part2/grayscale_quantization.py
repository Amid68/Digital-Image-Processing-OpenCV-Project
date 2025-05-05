import cv2
import numpy as np

def apply_grayscale_quantization(frame, levels=8):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bin_size = 256 // levels
    quantized = (gray // bin_size) * bin_size
    
    return cv2.cvtColor(quantized, cv2.COLOR_GRAY2BGR)
