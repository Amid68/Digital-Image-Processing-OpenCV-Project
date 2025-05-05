import cv2
import numpy as np


gray = cv2.imread('watermarked.jpg', cv2.IMREAD_GRAYSCALE)


cv2.imwrite("grayscale.jpg", gray)


cv2.imshow("Grayscale Image", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()


height, width = gray.shape
print(f"Image dimensions: {width}x{height}")
print("Color channels: 1 (Grayscale)")


print("Pixel Statistics:")
print(f"- Mean: {np.mean(gray):.2f}")
print(f"- Min: {np.min(gray)}")
print(f"- Max: {np.max(gray)}")
print(f"- Std Dev: {np.std(gray):.2f}")

