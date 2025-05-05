import cv2
import numpy as np
import sys
import os

# Import all filter modules
from edge_detection import apply_edge_detection
from grayscale_quantization import apply_grayscale_quantization
from contrast_enhancement import apply_contrast_enhancement
from soft_appearance import apply_soft_appearance
from cartoon_filter import apply_cartoon_filter

def main():
    # Initialize camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    # Current filter mode
    current_mode = 0
    modes = ["Normal", "Edge Detection", "Grayscale Quantization", 
             "Contrast Enhancement", "Soft Appearance", "Cartoon Filter"]
    
    print("\n=== Camera Filter Application ===")
    print("Controls:")
    print("  0-5: Select filter mode")
    print("  Q/q: Quit")
    print("\nAvailable modes:")
    for i, mode in enumerate(modes):
        print(f"  {i}: {mode}")
    
    while True:
        # Capture frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image")
            break
        
        # Process frame based on selected mode
        if current_mode == 0:  # Normal mode
            processed_frame = frame
            info_text = "Mode: Normal"
        elif current_mode == 1:  # Edge Detection
            processed_frame = apply_edge_detection(frame)
            info_text = "Mode: Edge Detection"
        elif current_mode == 2:  # Grayscale Quantization
            processed_frame = apply_grayscale_quantization(frame)
            info_text = "Mode: Grayscale Quantization"
        elif current_mode == 3:  # Contrast Enhancement
            processed_frame = apply_contrast_enhancement(frame)
            info_text = "Mode: Contrast Enhancement"
        elif current_mode == 4:  # Soft Appearance
            processed_frame = apply_soft_appearance(frame)
            info_text = "Mode: Soft Appearance"
        elif current_mode == 5:  # Cartoon Filter
            processed_frame = apply_cartoon_filter(frame)
            info_text = "Mode: Cartoon Filter"
        
        # Add info text to the frame
        cv2.putText(processed_frame, info_text, (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # Display the resulting frame
        cv2.imshow('Camera Filter Application', processed_frame)
        
        # Handle key press
        key = cv2.waitKey(1) & 0xFF
        
        # Mode selection (0-5)
        if ord('0') <= key <= ord('5'):
            current_mode = key - ord('0')
            print(f"Switched to mode: {modes[current_mode]}")
        
        # Quit
        elif key == ord('q'):
            break
    
    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
