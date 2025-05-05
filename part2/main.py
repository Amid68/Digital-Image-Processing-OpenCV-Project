import cv2
import numpy as np
import sys
import os
from edge_detection import apply_edge_detection
from grayscale_quantization import apply_grayscale_quantization
from contrast_enhancement import apply_contrast_enhancement
from soft_appearance import apply_soft_appearance
from cartoon_filter import apply_cartoon_filter

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error! Can't open camera.")
        return
    
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
        ret, frame = cap.read()
        if not ret:
            print("Error! Can't capture image")
            break
        
        if current_mode == 0:
            processed_frame = frame
            info_text = "Mode: Normal"
        elif current_mode == 1: 
            processed_frame = apply_edge_detection(frame)
            info_text = "Mode: Edge Detection"
        elif current_mode == 2:
            processed_frame = apply_grayscale_quantization(frame)
            info_text = "Mode: Grayscale Quantization"
        elif current_mode == 3: 
            processed_frame = apply_contrast_enhancement(frame)
            info_text = "Mode: Contrast Enhancement"
        elif current_mode == 4:
            processed_frame = apply_soft_appearance(frame)
            info_text = "Mode: Soft Appearance"
        elif current_mode == 5: 
            processed_frame = apply_cartoon_filter(frame)
            info_text = "Mode: Cartoon Filter"
        
        cv2.putText(processed_frame, info_text, (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.imshow('Camera Filter Application', processed_frame)
        key = cv2.waitKey(1) & 0xFF
        if ord('0') <= key <= ord('5'):
            current_mode = key - ord('0')
            print(f"Switched to mode: {modes[current_mode]}")
        
        elif key == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
