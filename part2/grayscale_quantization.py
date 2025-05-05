import cv2
import numpy as np

def apply_grayscale_quantization(frame, levels=8):
    """Reduce grayscale to specified number of levels"""
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Calculate bin size for quantization
    bin_size = 256 // levels
    
    # Apply quantization
    quantized = (gray // bin_size) * bin_size
    
    # Convert back to BGR for display
    return cv2.cvtColor(quantized, cv2.COLOR_GRAY2BGR)
