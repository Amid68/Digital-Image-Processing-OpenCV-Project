import cv2
import numpy as np
import matplotlib.pyplot as plt


brightened = cv2.imread('brightness_modified.jpg', cv2.IMREAD_GRAYSCALE)


corrected = cv2.equalizeHist(brightened)


cv2.imshow("Brightness Modified", brightened)
cv2.imshow("Corrected Image", corrected)
cv2.imwrite("brightness_corrected.jpg", corrected)
cv2.waitKey(0)
cv2.destroyAllWindows()


plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.hist(brightened.ravel(), bins=256, range=(0, 256), color='gray')
plt.title("Before Correction")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
plt.hist(corrected.ravel(), bins=256, range=(0, 256), color='blue')
plt.title("After Histogram Equalization")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
